import pandas as pd

df = pd.read_csv('TrilhaDadosJR-JUN15/Desafio/vendas_cursos.csv')

print("Primeiras linhas do conjunto de dados:")
print(df.head())

print("\nInformações básicas do conjunto de dados:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

df['Receita'] = df['Quantidade de Vendas'] * df['Preço Unitário']
receita_total = df['Receita'].sum()
print(f"\nReceita total gerada: R$ {receita_total:.2f}")

curso_mais_vendido = df.loc[df['Quantidade de Vendas'].idxmax()]['Nome do Curso']
vendas_curso_mais_vendido = df['Quantidade de Vendas'].max()
print(f"\nCurso com maior número de vendas: {curso_mais_vendido} ({vendas_curso_mais_vendido} vendas)")


