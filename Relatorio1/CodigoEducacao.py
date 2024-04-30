import pandas as pd

#Carrega as bases de dados
alunos = pd.read_csv('basedealunos9.csv', delimiter=';')
dengue = pd.read_csv('basededengue9.csv', delimiter=';')

#Identificar os alunos que não tiveram dengue
alunos_sem_dengue = alunos[~alunos['ID'].isin(dengue['ID'])]

# Selecionar apenas as colunas 'Nome', 'Data de Nascimento' e 'ID'
nova_base = alunos_sem_dengue[['Nome', 'Data de Nascimento', 'ID']]

#Salva a nova base de dados e printa uma mensagem de conclusão
nova_base.to_csv('nova_base.csv', index=False)
print("Nova base de dados criada com sucesso!")
