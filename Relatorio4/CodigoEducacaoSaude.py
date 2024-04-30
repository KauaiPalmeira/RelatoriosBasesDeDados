import pandas as pd

# Carregar a base de dados
alunos = pd.read_csv('basedealunos9.csv', delimiter=';')
dengue = pd.read_csv('basededengue9.csv', delimiter=';')

# Identificar quem teve dengue e quem foi a escola
cidadaos_escola = set(alunos['ID'])
cidadaos_dengue = set(dengue['ID'])

# Interseção entre quem que frequentou a escola e quem que teve dengue
cidadaos_educacao_saude = cidadaos_escola.intersection(cidadaos_dengue)

# Filtrar os dados dos cidadãos do relatorio
dados_educacao_saude = alunos[alunos['ID'].isin(cidadaos_educacao_saude)]
# Adicionar a data de dengue aos dados do relatorio
dados_educacao_saude = pd.merge(dados_educacao_saude, dengue[['ID', 'Data da Dengue']], on='ID')

# Salva e conclui
dados_educacao_saude.to_csv('relatorio_educacao_saude.csv', columns=['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue'], index=False)
print("Relatório Educação e Saúde criado com sucesso!")
