import pandas as pd

# Carregar os dados das duas tabelas
tabela1 = pd.read_csv("basededengue9.csv", delimiter=";")
tabela2 = pd.read_csv("basedealunos9.csv", delimiter=";")
tabela3 = pd.read_csv("basedeonibus9.csv", delimiter=";", encoding='latin-1')


# Realizar o merge usando mais de uma chave
merged = pd.merge(tabela1, tabela2, on=['Nome', 'Nome da Mae', 'Nome do Pai'], how='left')
mergedFinal = pd.merge(merged, tabela3, on=['Nome', 'Nome da Mae', 'Nome do Pai'], how='left')

# Exibir o resultado
mergedFinal.to_csv('relatorio_saude_sem_escola_nem_transporte.csv', columns=['Nome', 'Data da Dengue'], index=False)
print("Relatório Saúde sem Mobilidade criado com sucesso!")