import pandas as pd

# Carrega as bases de dengue, onibus e alunos
dengue = pd.read_csv('basededengue9.csv', delimiter=';')
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')
alunos = pd.read_csv('basedealunos9.csv', delimiter=';')

# Identifica quem foi ao posto de saude
cidadaos_saude = set(dengue['ID'])

# Identifica quem usou onibus
cidadaos_onibus = set()
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

# Identificar quem foi pra escola
cidadaos_escola = set(alunos['ID'])

# Interseção entre os cidadãos que frequentaram o posto de saude, a escola e usam onibus
cidadaos_saude_mobilidade_educacao = cidadaos_saude.intersection(cidadaos_onibus).intersection(cidadaos_escola)

# Filtrar os dados dos cidadãos
dados_saude_mobilidade_educacao = dengue[dengue['ID'].isin(cidadaos_saude_mobilidade_educacao)]
# Adicionar as linhas de ônibus
dados_saude_mobilidade_educacao = pd.merge(dados_saude_mobilidade_educacao, onibus[['ID', 'Ônibus']], on='ID')

# Salvar e conclui
dados_saude_mobilidade_educacao.to_csv('relatorio_saude_mobilidade_educacao.csv', columns=['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue', 'Ônibus'], index=False)
print("Relatório Saúde, Mobilidade e Educação criado com sucesso!")
