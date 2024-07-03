import pandas as pd

df = pd.read_csv('TrilhaDadosJR-JUN15/Desafio/vendas_cursos.csv')

print("Primeiras linhas do conjunto de dados:")
print(df.head())

print("\nInformações básicas do conjunto de dados:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

