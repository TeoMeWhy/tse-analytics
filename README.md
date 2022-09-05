# Análise dos partidos e candidatos para Elições de 2022

# Análise dos partidos e candidatos para Elições de 2022

Dados coletados a partir do site do TSE: [https://divulgacandcontas.tse.jus.br/divulga/#/](https://divulgacandcontas.tse.jus.br/divulga/#/)

## Índice

- [1. ETL](#1-etl)

## 1. ETL

Antes de nos debruçarmos diretamente em gráficos e análises, precisamos realizar o ETL (Extract Transform and Load), isto é, consultar os dados brutos e realizar os devidos filtros, cruzamentos e agregações. 
Desta maneira, como nosso intuito é realizar no primeiro momento uma análise voltada aos partidos, vamos agregar todas as informações dos candidatos por seus respectivos partidos.

Segue abaixo as estatísticas criadas a partir dos dados brutos:

|Nome Variável|Descrição|
|---|---|
| QTD_CANDIDATOS | Quantidade de candidatos no partido|
| PCT_MASCULINO | Percentual de candidatos do gênero masculino no partido|
| PCT_FEMININO | Percentual de candidatas do gênero feminino no partido|
| PCT_LE_ESCREVE | Percentual de candidatos que tem como "Sabe ler e escrever" como Grau de Instrução no partido |
| PCT_FUNDAMENTAL_INCOMPLETO | Percentual de candidatos que tem como "Ensino Fundamental Incompleto" como Grau de Instrução no partido |
| PCT_FUNDAMENTAL_COMPLETO | Percentual de candidatos que tem como "Ensino Fundamental Completo" como Grau de Instrução no partido |
| PCT_MEDIO_INCOMPLETO | Percentual de candidatos que tem como "Ensino Médio Incompleto" como Grau de Instrução no partido |
| PCT_MEDIO_COMPLETO | Percentual de candidatos que tem como "Ensino Médio Completo" como Grau de Instrução no partido |
| PCT_SUPERIOR_INCOMPLETO | Percentual de candidatos que tem como "Ensino Superior Incompleto" como Grau de Instrução no partido |
| PCT_SUPERIOR_COMPLETO | Percentual de candidatos que tem como "Ensino Superior Completo" como Grau de Instrução no partido |
| PCT_SOLTEIRO | Percentual de solteiros no partido |
| PCT_CASADO | Percentual de casados no partido |
| PCT_SEPARADO_JUDICIALMENTE | Percentual de Separados Judicialmente no partido|
| PCT_DIVORCIADO | Percendual de Divorciados no partido |
| PCT_VIUVO | Percentual de Viúvos no partido|
| PCT_AMARELA | Percentual de "cor e raça" amarela no partido|
| PCT_BRANCA | Percentual de "cor e raça" branca no partido|
| PCT_INDiGENA | Percentual de "cor e raça" indígena no partido|
| PCT_PARDA | Percentual de "cor e raça" parda no partido|
| PCT_PRETA | Percentual de "cor e raça" preta no partido|
| AVG_IDADE | Média de idade no partido|

