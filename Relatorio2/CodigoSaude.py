import pandas as pd

# Leitura da base de dados do posto de saúde com codificação Latin-1 pq sem especificar -
# a codificacao tava bugando
onibus = pd.read_csv('basedeonibus9.csv', delimiter=';', encoding='latin-1')


cidadaos_onibus = set()

#Itera sobre as linhas da base de dados do posto de saude
#Itera sobre as linhas da coluna 'Ônibus' e em seguida adiciona o ID do cidadão
for index, row in onibus.iterrows():
    for bus in row['Ônibus'].split(', '):
        cidadaos_onibus.add(int(bus))

#le a base
dengue = pd.read_csv('basededengue9.csv', delimiter=';')

# Armazena ID de quem tem dengue
cidadaos_dengue = set(dengue['ID'])
# Interseção de quem teve dengue com quem andou de onibus
cidadaos_saude = cidadaos_onibus.intersection(cidadaos_dengue)

# Filtragem dos dados dos cidadaos que frequentaram o posto de saude e utilizaram transporte publico
dados_saude = onibus[onibus['ID'].isin(cidadaos_saude)]


#Salva o relatorio e conclui
dados_saude.to_csv('relatorio_saude.csv', columns=['Nome', 'Data de Nascimento', 'ID'], index=False)
print("Relatório de Saúde criado com sucesso!")
