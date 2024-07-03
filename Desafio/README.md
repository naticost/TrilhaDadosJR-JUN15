
# Análise de Vendas de Cursos 📊

Este repositório apresenta análises e visualizações das vendas de cursos, utilizando dados de um arquivo CSV.

## Dados Utilizados 📑

Os dados estão armazenados no arquivo `vendas_cursos.csv` e incluem as seguintes colunas:

- **ID**: Identificador único do curso.
- **Nome do Curso**: Nome do curso vendido.
- **Quantidade de Vendas**: Número de unidades vendidas de cada curso.
- **Preço Unitário**: Preço por unidade do curso.
- **Data**: Data da venda.

## Análise Realizada 📈

### Estatísticas Básicas e Receita Total

Foram calculadas estatísticas descritivas dos dados, como média, desvio padrão, mínimo e máximo das quantidades vendidas e preços unitários. A receita total gerada pela venda de cursos foi calculada somando a multiplicação da quantidade de vendas pelo preço unitário de cada curso.

### Gráficos Gerados 📊

#### Número de Vendas por Curso

Um gráfico de barras foi criado para mostrar o número de vendas para cada curso. As barras são coloridas usando a paleta de cores 'viridis' do seaborn.

![Número de Vendas por Curso](num_vendas_por_curso.png)

#### Relação entre Quantidade de Vendas e Preço Unitário

Um gráfico de dispersão foi utilizado para visualizar a relação entre a quantidade de vendas e o preço unitário de cada curso. Cada ponto no gráfico representa um curso, colorido de acordo com o nome do curso usando a paleta de cores 'Set2'.

![Relação entre Quantidade de Vendas e Preço Unitário](relacao_vendas_preco.png)

## Conclusões

**Gráfico de Barras: Número de Vendas por Curso**
- O curso mais vendido é "Introdução à Programação em Python", com aproximadamente 45 vendas.
- "Desenvolvimento Web com HTML e CSS" e "Cloud Computing com AWS" também possuem um bom número de vendas, cada um com mais de 25 unidades vendidas.
- "JavaScript Avançado: Frameworks e Bibliotecas" e "Desenvolvimento Mobile com React Native" estão na faixa intermediária, com vendas consideráveis.
- Cursos como "Segurança da Informação: Fundamentos" e "DevOps: Integração e Entrega Contínua" têm menos de 20 vendas cada.

**Gráfico de Dispersão: Relação entre Quantidade de Vendas e Preço Unitário**
- Existe uma tendência de que cursos com preços mais baixos têm um número maior de vendas.
- "Introdução à Programação em Python" destaca-se com um alto número de vendas e um preço unitário relativamente baixo.
- Cursos com preços unitários mais altos, como "Cloud Computing com AWS" e "Desenvolvimento Mobile com React Native", têm menos vendas, confirmando a tendência inversa entre preço e quantidade de vendas.
- Cursos com preços intermediários mostram uma distribuição mais dispersa, sugerindo que outros fatores além do preço podem influenciar as vendas.
