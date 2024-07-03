import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

caminho = 'TrilhaDadosJR-JUN15/Desafio/vendas_cursos.csv'
df = pd.read_csv(caminho)

plt.figure(figsize=(10, 6))
sns.barplot(x='Nome do Curso', y='Quantidade de Vendas', data=df, palette='viridis')
plt.xticks(rotation=90)
plt.title('Número de Vendas por Curso')
plt.tight_layout()
plt.savefig('num_vendas_por_curso.png')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Preço Unitário', y='Quantidade de Vendas', data=df, hue='Nome do Curso', palette='Set2')
plt.title('Relação entre Quantidade de Vendas e Preço Unitário')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de Vendas')
plt.tight_layout()
plt.savefig('relacao_vendas_preco.png') 
plt.show()