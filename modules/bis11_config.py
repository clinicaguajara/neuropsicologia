# bis11_config.py

# ===============================
# Questões do Questionário BIS-11
# ===============================
questions_bis11 = [
    {"id": i+1, "question": q["question"], "options": q["options"]}
    for i, q in enumerate([
        {"question": "Eu planejo tarefas cuidadosamente.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu faço coisas sem pensar.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu tomo decisões rapidamente.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu sou despreocupado (confio na sorte, 'desencanado').", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu não presto atenção.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu tenho pensamentos que se atropelam.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu planejo viagens com bastante antecedência.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu tenho autocontrole.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu me concentro facilmente.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu economizo (poupo) regularmente.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu fico me contorcendo na cadeira em peças de teatro ou palestras.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu penso nas coisas com cuidado.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu faço planos para me manter no emprego (eu cuido para não perder meu emprego).", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu falo coisas sem pensar.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu gosto de pensar em problemas complexos.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu troco de emprego.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu ajo por impulso.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu fico entediado com facilidade quando estou resolvendo problemas mentalmente.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu ajo no 'calor' do momento.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu mantenho a linha de raciocínio ('não perco o fio da meada').", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu troco de casa (residência).", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu compro coisas por impulso.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu só consigo pensar em uma coisa de cada vez.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu troco de interesses e passatempos ('hobby').", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu gasto ou compro a prestação mais do que ganho.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Enquanto estou pensando em uma coisa, é comum que outras ideias me venham à cabeça ou ao mesmo tempo.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu tenho mais interesse no presente do que no futuro.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu me sinto inquieto em palestras ou aulas.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu gosto de jogos e desafios mentais.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]},
        {"question": "Eu me preparo para o futuro.", "options": ["Raramente ou nunca", "Às vezes", "Frequentemente", "Sempre ou quase sempre"]}
    ])
]

# ===============================
# Normas, mapeamento e correção
# ===============================

percentile_table_bis11 = {
    "Attention": [5, 6, 7, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 13, 13, 14, 16, 18],
    "Cognitive Instability": [3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 10, 12],
    "Motor": [7, 8, 9, 9, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 15, 15, 16, 18, 20, 23],
    "Perseverance": [4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10, 12],
    "Cognitive Complexity": [6, 8, 9, 9, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 18],
    "Self-Control": [6, 8, 9, 10, 10, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16, 17, 18, 19, 22],
    "Total": [40, 47, 50, 52, 53, 55, 56, 58, 59, 60, 62, 63, 64, 65, 67, 68, 70, 72, 76, 80, 90]
}

percentile_indices_bis11 = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 99]

itens_para_inverter = [1, 7, 8, 9, 10, 12, 13, 15, 20, 29, 30]

answer_map = {
    "Raramente ou nunca": 1,
    "Às vezes": 2,
    "Frequentemente": 3,
    "Sempre ou quase sempre": 4
}

subscale_mapping = {
    "Attention": [5, 9, 11, 20, 28],
    "Cognitive Instability": [6, 24, 26],
    "Motor": [2, 3, 4, 17, 19, 22],
    "Perseverance": [16, 21, 23],
    "Cognitive Complexity": [10, 15, 18, 27, 29],
    "Self-Control": [1, 7, 8, 12, 13, 14, 30]
}

def find_percentile_interval(score, factor, percentile_table, percentile_indices):
    normative_scores = percentile_table[factor]
    matching_indexes = [i for i, val in enumerate(normative_scores) if val == score]
    if matching_indexes:
        matched_percentiles = [percentile_indices[i] for i in matching_indexes]
        return f"{min(matched_percentiles)}" if len(matched_percentiles) == 1 else f"{min(matched_percentiles)}-{max(matched_percentiles)}"
    for i, val in enumerate(normative_scores):
        if score < val:
            if i == 0:
                return f"0-{percentile_indices[0]}"
            else:
                return f"{percentile_indices[i-1]}-{percentile_indices[i]}"
    return f"{percentile_indices[-2]}-100"

def automated_correction_bis11(answers, normative_table, percentile_indices):
    numeric_answers = {}
    for key, value in answers.items():
        question_num = int(key.split("_")[1])
        base_value = answer_map.get(value, 0)
        if question_num in itens_para_inverter:
            base_value = 5 - base_value
        numeric_answers[question_num] = base_value

    scores = {factor: sum(numeric_answers.get(i, 0) for i in items) for factor, items in subscale_mapping.items()}
    total_score = sum(numeric_answers.get(i, 0) for i in range(1, 31))
    scores["Total"] = total_score

    report = {}
    for factor in normative_table:
        if factor in scores:
            score = scores[factor]
            percentile = find_percentile_interval(score, factor, normative_table, percentile_indices)
            report[factor] = {"score": score, "percentile": percentile}
    return report