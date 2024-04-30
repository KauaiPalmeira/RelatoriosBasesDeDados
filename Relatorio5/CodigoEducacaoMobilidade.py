import pandas as pd

# Carregar a base de dados dos alunos e de onibus
alunos = pd.read_csv('basedealunos9.csv', delimiter=';')
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')

# Identificar quem frequenta a escola
cidadaos_escola = set(alunos['ID'])

# Identificar os cidadãos que utilizaram transporte público
cidadaos_onibus = set()
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

# Interseção entre os cidadãos que frequentaram a escola e os que utilizaram transporte público
cidadaos_educacao_mobilidade = cidadaos_escola.intersection(cidadaos_onibus)

# Filtrar os dados dos cidadãos do relatorio
dados_educacao_mobilidade = alunos[alunos['ID'].isin(cidadaos_educacao_mobilidade)]

# Adicionar as linhas de ônibus aos relatorio
dados_educacao_mobilidade = pd.merge(dados_educacao_mobilidade, onibus[['ID', 'Ônibus']], on='ID')

# Salvar e conclui
dados_educacao_mobilidade.to_csv('relatorio_educacao_mobilidade.csv', columns=['Nome', 'Data de Nascimento', 'ID', 'Ônibus'], index=False)
print("Relatório Educação e Mobilidade criado com sucesso!")
