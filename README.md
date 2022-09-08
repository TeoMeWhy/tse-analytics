# Análise dos partidos e candidatos para Eleições de 2022

Dados coletados a partir do site do TSE: [dadosabertos.tse.jus.br/dataset/candidatos-2022](https://dadosabertos.tse.jus.br/dataset/candidatos-2022), armazenados e analisados durante as lives no canal [Téo Me Why](https://www.twitch.tv/teomewhy).

Segue os VODs para acompanhar o desenvolvimento:

| Dia | Descrição| Link |
|---|---|---|
|2022-09-05| Análise de Bens e Clusters de Diversidade dos partidos |[:link:](https://www.twitch.tv/videos/1583439007) |
|2022-09-07| Correções nas médias de taxas para a taxa geral. Mudança de representação gráfica. Novas bases adicionadas |[:link:]([https://www.twitch.tv/videos/1583439007](https://www.twitch.tv/videos/1584667854)) |

## Índice

- [1. ETL](#1-etl)
- [2. Análises](#2-análises)
    - [2.1. Bens Declarados](#21-bens-declarados)
    - [2.2. Clusters em Diversidade](#22-clusters-em-diversidade)

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
| VL_TOTAL_BEM_PARTIDO |Valor total declarado em bens dos candidatos do partido|
| AVG_BEM_CANDIDATO |Valor médio declarado por candidato do partido|
| MEDIAN_BEM_CANDIDATO |Valor mediano declarado por candidato do partido|
| MAX_BEM_CANDIDATO |Valor mais alto declarado do partido |

Todos estes dados foram criados e persistidos na tabela `silver_tse.sumario_partido` e seu script pode ser encontrado em `etl_sumario_partido.sql`.

## 2. Análises

## 2.1. Bens declarados

De maneira trivial, podemos gerar um (ou dois) gráficos bem simples para entender o comportamento dos partidos em relação à declaração de bens. isto é, calcular a **média** (AVG_BEM_CANDIDATO) e **mediana** (MEDIAN_BEM_CANDIDATO) por partido. Para média:

<img src="https://i.ibb.co/r7hwkCB/grupos-partidos-media-bens.jpg" alt="grupos-partidos-media-bens" width="750">

Agora para a mediana (menos sensível à dados afastados da média):

<img src="https://i.ibb.co/PNc5bSJ/grupos-partidos-mediana-bens.jpg" alt="grupos-partidos-mediana-bens" width="750">

Interessante como a ordem dos partidos no gráfico se altera quando utilizamos uma medida menos sensível à outliers.

## 2.2. Clusters em Diversidade

A partir da tabela criada anteriormente, dá-se início às análises. Com isso, a primeira ideia seria realizar agrupameneto entre os 33 partidos encontrados, buscando classificar partidos similares entre si em um mesmo grupo.

Utilizando as variáveis `PCT_FEMININO` e `PCT_PRETA`, aplicou-se o método de KMeans considerando 6 grupos. O resultado desta análise se dá pelo gráfico abaixo:

<img src="https://i.ibb.co/8dtNQ9n/grupos-partidos-diversidade.jpg" alt="grupos-partidos-diversidade" width="750">

Adicionamos também uma visão que considera o tamanho do partido, i.e., a quantidade de candidatos que este partido tem para essas eleições. O tamanho de cada bolha, diz a respeito da quantidade de candidatos presentes no partido:

<img src="https://i.ibb.co/8dN0JtW/grupos-partidos-diversidade-tamanho.jpg" alt="grupos-partidos-diversidade-tamanho" width="750">

Por fim, a mesma de forma análoga à quantidade de candidatos, realizamos para o valor mediano de bens em cada partido, onde este número reflete no tamanho de sua bolha.

<img src="https://i.ibb.co/WytRYMk/grupos-partidos-diversidade-bens.jpg" alt="grupos-partidos-diversidade-bens" width="750">

O que se pode interpretar deste agrupamento? Vamos tentar responder abaixo.

| Partidos | Resumo |
|---|---|
| Novo, PL, PCA (Sem partido) | Grupo que possui menor diversidade, tanto em gênero quanto em raça e cor.|
| PSD, PTB, UNIÃO, PSDB, PODE, Republicanos, PV, PRTB, Patriota, PP, PSC, Solidariedade, Avante, MDB, Cidadania, AGIR, PMN | Grupo que contém maior número de partidos. Possui proporções de mulheres abaixo da média mas cresce a proporção de raça preta.|
|DC, PSB, PROS, Rede, PMB, PDT, PCO| Grupo concentrado um pouco acima da proporção de raça preta geral, mas ainda abaixo da proporção de mulheres geral |
|PC do B, PCB, PT|Grupo com valores de diversidade mais altos do que a base geral, se distanciando dos grupos de posições inferiores do gráfico. Vale destacar que PC do B está relativamente distante dos outros dois partidos de seu grupo, uma vez que possui uma proporção de mulheres mais elevada.|
|PSOL, PSTU|Um dos menores grupos, com apenas 2 partidos, estes que apresentam a maior proporção de raça preta..|
|UP|Grupo com apenas um partido, pois este se destaca nitidamente por altas proporções de mulheres e raça preta, sendo o único que possui mais mulheres que homens em seu partido.|

