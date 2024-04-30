import pandas as pd

#Carrega as 3 bases de dados, de onibus precisa de encoding pq se não buga
alunos = pd.read_csv('basedealunos9.csv', delimiter=';')
dengue = pd.read_csv('basededengue9.csv', delimiter=';')
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')


# Identificar os cidadãos que utilizaram o transporte público
cidadaos_onibus = set()
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

# ID de quem tem dengue
cidadaos_dengue = set(dengue['ID'])

#Interseção entre os cidadãos que utilizaram o transporte público e os que não tiveram dengue
cidadaos_mobilidade = cidadaos_onibus.difference(cidadaos_dengue)

# Filtrar os dados dos cidadãos do Relatório de Mobilidade
dados_mobilidade = onibus[onibus['ID'].isin(cidadaos_mobilidade)]


#Salva o arquivo e printa
dados_mobilidade.to_csv('relatorio_mobilidade.csv', columns=['Nome', 'Data de Nascimento', 'Ônibus'], index=False)
print("Relatório de Mobilidade criado com sucesso!")
