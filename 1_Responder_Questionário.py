import streamlit as st
from supabase import create_client
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

from modules.bis11_config import (
    questions_bis11,
    automated_correction_bis11,
    percentile_table_bis11,
    percentile_indices_bis11
)
from modules.auth import get_supabase_client

st.set_page_config(page_title="Neuropsicologia 🧠", layout="centered")
st.title("📝 Dinâmica de Neuropsicologia")
st.divider()
st.write("Responda o formulário a seguir para participar da dinâmica. Suas respostas serão utilizadas em sala de aula de forma anônima.")
st.write("📌 ATENÇÃO: Não esqueça de fazer o download da tabela ou tirar um print para usar em sala de aula!")
st.divider()
supabase = get_supabase_client()

with st.form("formulario_bis11"):
    nome = st.text_input("Nome completo (apenas para registro)", key="nome_completo")
    respostas = {}

    for item in questions_bis11:
        opcoes = ["Selecione..."] + item["options"]
        resposta = st.radio(
            f"{item['id']}. {item['question']}",
            opcoes,
            key=f"question_{item['id']}"
        )
        respostas[f"question_{item['id']}"] = resposta

    enviado = st.form_submit_button("Enviar Respostas")

if enviado:
    if not nome.strip():
        st.warning("Por favor, insira seu nome completo.")
        st.stop()

    if any(resp == "Selecione..." for resp in respostas.values()):
        st.warning("Por favor, responda todas as questões antes de enviar.")
        st.stop()

    resultado = automated_correction_bis11(respostas, percentile_table_bis11, percentile_indices_bis11)

    # Salvar no Supabase
    supabase.table("bis11_respostas").insert({
        "nome_completo": nome,
        "respostas": respostas,
        "pontuacoes": resultado
    }).execute()

    st.success("✅ Questionário enviado com sucesso!")
    st.divider()
    st.subheader(f"📊 Resultados de: {nome}")

    # Tabela de resultados
    dados = [
        {
            "Fator": str(fator),
            "Pontuação": str(info["score"]),
            "Percentil": str(info["percentile"])
        }
        for fator, info in resultado.items()
    ]

    df = pd.DataFrame(dados).astype(str)

    # 🎨 Gerar imagem da tabela com matplotlib
    fig, ax = plt.subplots(figsize=(8, 2 + 0.5 * len(df)))  # ajusta a altura
    ax.axis("off")
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    # Salvar em memória como PNG
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", dpi=300)
    buf.seek(0)

    # 📥 Botão de download da imagem
    st.download_button(
        label="🖼️ Baixar imagem da tabela (.png)",
        data=buf,
        file_name=f"resultado_bis11_{nome.replace(' ', '_').lower()}.png",
        mime="image/png"
    )

    st.table(df)

    st.write("📌 ATENÇÃO: Não esqueça de fazer o download da tabela ou tirar um print para usar em sala de aula!")
