import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
import plotly.express as px
import plotly.graph_objects as go

from modules.auth import get_supabase_client

st.set_page_config(page_title="Distribuição Estatística", layout="wide")
st.title("📊 Distribuição Estatística")

# Supabase client
supabase = get_supabase_client()

# 🔄 Carregar dados
with st.spinner("Carregando dados..."):
    response = supabase.table("bis11_respostas").select("nome_completo, pontuacoes").execute()
    dados = response.data or []

if not dados:
    st.warning("Nenhum dado encontrado na tabela 'bis11_respostas'.")
    st.stop()

# 🔢 Processar dados
registros = []

for entry in dados:
    nome = entry["nome_completo"]
    pontuacoes = entry.get("pontuacoes", {})
    for fator, info in pontuacoes.items():
        registros.append({
            "Participante": nome,
            "Fator": fator,
            "Pontuação": info["score"]
        })

df = pd.DataFrame(registros)

# 📦 Boxplot por fator
st.subheader("📦 Boxplot por Fator")

fig_box = px.box(df, x="Fator", y="Pontuação", points="all", color="Fator")
st.plotly_chart(fig_box, use_container_width=True)

# 📈 Distribuição do escore total
st.subheader("📈 Distribuição do Escore Total")

df_total = df[df["Fator"] == "Total"]
pontuacoes_total = df_total["Pontuação"].astype(float)

# Calcular densidade com scipy
kde = gaussian_kde(pontuacoes_total)
x_vals = np.linspace(pontuacoes_total.min(), pontuacoes_total.max(), 200)
y_vals = kde(x_vals)

# Criar gráfico com histograma e curva
fig_hist = go.Figure()

fig_hist.add_trace(go.Histogram(
    x=pontuacoes_total,
    histnorm="probability density",
    name="Histograma",
    opacity=0.6
))

fig_hist.add_trace(go.Scatter(
    x=x_vals,
    y=y_vals,
    mode="lines",
    name="Curva de Densidade",
    line=dict(color="red")
))

fig_hist.update_layout(
    xaxis_title="Escore Total",
    yaxis_title="Densidade",
    title="Distribuição Normal Estimada do Escore Total",
    showlegend=True
)

st.plotly_chart(fig_hist, use_container_width=True)

st.write("📊 Número de participantes:", len(pontuacoes_total))
