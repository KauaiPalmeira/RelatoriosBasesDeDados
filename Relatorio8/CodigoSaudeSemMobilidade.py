import pandas as pd

# Carregar a base de dados de saude e bus
dengue = pd.read_csv('basededengue9.csv', delimiter=';')
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')

# Identificar quem foi no posto d saude
cidadaos_saude = set(dengue['ID'])

# identifica quem usa onibus
cidadaos_onibus = set()
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

# Identificar os cidadãos que frequentaram o posto de saúde mas nao usa onibus
cidadaos_saude_sem_mobilidade = cidadaos_saude.difference(cidadaos_onibus)

# Filtrar os dados dos cidadãos pro relatorio
dados_saude_sem_mobilidade = dengue[dengue['ID'].isin(cidadaos_saude_sem_mobilidade)]

# Salvar e conclui
dados_saude_sem_mobilidade.to_csv('relatorio_saude_sem_mobilidade.csv', columns=['Nome', 'Data de Nascimento', 'ID', 'Data da Dengue'], index=False)
print("Relatório Saúde sem Mobilidade criado com sucesso!")
