# Relatório

## Autores

**Arthur Rocha Amaral**

**Guilherme Oliveira Antônio**

---

## Introdução

Este trabalho tem o intuito de estudar os repositórios populares do GitHub. Dessa maneira, sera analisado o desenvolvimento, frequência de contribuição externa, frequência de lançamento de release, popularidade, tempo de existência do repositório, linguagem primaria usadas e total de issues fechadas. Com o intuito de atingir o objetivo de encontrar os projetos populares, sera buscado os 1000 repositórios com mais estrelas. Assim, como mecanismo de busca de dados necessários para análise sera usado o mecanismo de busca do GitHub com Graphql.

---

## Metodologia

Para obtermos os dados a serem avaliados, buscamos da API GraphQL do GitHub os repositórios ordenados em ordem decrescente pela quantidade de estrelas, listados em páginas de 100 items, assim, pegaremos as 10 primeiras páginas com os dados necessários para respondermos as questões de pesquisa. Após o recebimento dos dados, filtramos os dados inconsistentes e salvamos o resultado em um arquivo CSV como feito na sprint 2 desse projeto.

Após dados filtrados, mapeados e armazenados, utilizamos esses para criar os gráficos que ilustram os valor obtidos e com os quais chegaremos as respostas.

---

## Discussão/Hipóteses/Valores obtidos

### RQ Q1 - Qual a relação entre a popularidade dos repositórios e as suas características de qualidade?

***Estrelas x Lcom***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

***Estrelas x CBO***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>
    
***Estrelas x DIT***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

### RQ Q2 - Qual a relação entre a maturidade do repositórios e as suas características de qualidade ?

***Idade x Lcom***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

***Idade x CBO***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>
    
***Idade x DIT***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

### RQ Q3 - Qual a relação entre a atividade dos repositórios e as suas características de qualidade?  

***Releases x Lcom***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

***Releases x CBO***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>
    
***Releases x DIT***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

### RQ Q4 - Qual a relação entre o tamanho dos repositórios e as suas características de qualidade?  

***LOC x Lcom***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>

***LOC x CBO***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>
    
***LOC x DIT***

- **Hipótese**:
- **Resultados**:

    <div style="text-align: center"><img src="assets/Q1.png" alt="RQ Q1 Gráfico"></div>