import pandas as pd

# Carregar a base de dados de dengue e onibus
dengue = pd.read_csv('basededengue9.csv', delimiter=';')
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')

# Identificar quem foi ao posto de saude
cidadaos_saude = set(dengue['ID'])

# Identificar os cidadãos que utilizaram onibus
cidadaos_onibus = set()
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

# Fazer a interseção entre os cidadãos que frequentaram o posto de saúde e os que utilizaram transporte público
cidadaos_saude_mobilidade = cidadaos_saude.intersection(cidadaos_onibus)

# Filtrar os dados dos cidadãos
dados_saude_mobilidade = dengue[dengue['ID'].isin(cidadaos_saude_mobilidade)]

# Adicionar as linhas de ônibus ao relatorio
dados_saude_mobilidade = pd.merge(dados_saude_mobilidade, onibus[['ID', 'Ônibus']], on='ID')

# Salva e conclui
dados_saude_mobilidade.to_csv('relatorio_saude_mobilidade.csv', columns=['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue', 'Ônibus'], index=False)
print("Relatório Saúde e Mobilidade criado com sucesso!")
