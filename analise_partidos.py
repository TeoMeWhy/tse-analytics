# Databricks notebook source
# MAGIC %pip install bokeh adjustText

# COMMAND ----------

from sklearn import cluster
from bokeh.plotting import figure, output_file, save
from bokeh.io import show
import matplotlib.pyplot as plt
import numpy as np

from adjustText import adjust_text

import seaborn as sns

import os

# COMMAND ----------

df = spark.table("silver_tse.sumario_partido").toPandas()
df_geral = spark.table("bronze_tse.consulta_cand_2022_brasil")

# COMMAND ----------

df_count_genero = df_geral.groupBy("DS_GENERO").count().toPandas()
df_count_genero["proporcao"] = df_count_genero["count"] / df_count_genero["count"].sum()
taxa_mulheres = df_count_genero['proporcao'][df_count_genero['DS_GENERO']=='FEMININO'].values[0]
print("Taxa geral Mulheres:", taxa_mulheres)

df_count_cor_raca = df_geral.groupBy("DS_COR_RACA").count().toPandas()
df_count_cor_raca["proporcao"] = df_count_cor_raca["count"] / df_count_cor_raca["count"].sum()
taxa_preta = df_count_cor_raca['proporcao'][df_count_cor_raca['DS_COR_RACA']=='PRETA'].values[0]
print("Taxa Geral Preta:",taxa_preta)

# COMMAND ----------

# DBTITLE 1,Clusters Partidos
features = ['PCT_FEMININO','PCT_PRETA']

model = cluster.KMeans(n_clusters=6, random_state=1992)

model.fit(df[features])
df['cluster'] = model.labels_

# COMMAND ----------

df_cluster = df.groupby('cluster')[features].mean().reset_index()
df_cluster = df_cluster.merge( df.groupby('cluster')[['SG_PARTIDO']].count().reset_index() )
df_cluster

# COMMAND ----------

colors = (df['cluster'] + 1).tolist()

plt.figure(dpi=300)

plt.scatter(df['PCT_FEMININO'],
            df['PCT_PRETA'],
            c=colors,
            alpha=0.8)

texts = []

lines = zip(df['PCT_FEMININO'].tolist(),
           df['PCT_PRETA'].tolist(),
           df["SG_PARTIDO"].tolist())

for x, y, s in lines:
    texts.append(plt.text(x, y, s, fontsize=8))
    
plt.grid(True)
plt.suptitle("Grupos de Partidos - Candidatos 2022")
plt.title("Cores iguais representam partidos de mesmo grupo", fontsize=7)
plt.xlabel("Taxa de Mulheres")
plt.ylabel("Taxa de Raça Preta")
plt.ylim(0,0.42)

plt.vlines( taxa_mulheres, 0, 0.42, label='Taxa Mulheres Geral', linestyles='--', color = 'tomato')
plt.hlines( taxa_preta, 0.22, 0.65, label='Taxa Raça Preta Geral', linestyles='--', color= 'royalblue' )

adjust_text(texts, force_points=0.2, force_text=0.2,
            expand_points=(1, 1), expand_text=(1, 1),
            arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

plt.legend(fontsize=7, loc=4)

plt.text(0.2, -0.1, "Fonte: https://dadosabertos.tse.jus.br/dataset/candidatos-2022", fontsize=6)

plt.savefig("/dbfs/mnt/datalake/tmp/grupos_partidos_diversidade.jpeg", dpi=300, transparent=False)

# COMMAND ----------

colors = (df['cluster'] + 1).tolist()

plt.figure(dpi=300)

plt.scatter(df['PCT_FEMININO'],
            df['PCT_PRETA'],
            s=1.5*100*(df['qtCandidatos'] / df['qtCandidatos'].max()),
            c=colors,
            alpha=0.4)

texts = []

lines = zip(df['PCT_FEMININO'].tolist(),
           df['PCT_PRETA'].tolist(),
           df["SG_PARTIDO"].tolist())

for x, y, s in lines:
    texts.append(plt.text(x, y, s, fontsize=8))
    
plt.grid(True)
plt.suptitle("Grupos de Partidos - Candidatos 2022")
plt.title("Quanto maior a bolha, mais candidatos", fontsize=7)
plt.xlabel("Taxa de Mulheres")
plt.ylabel("Taxa de Raça Preta")
plt.ylim(0,0.42)

plt.vlines( taxa_mulheres, 0, 0.42, label='Taxa Mulheres Geral', linestyles='--', color = 'tomato')
plt.hlines( taxa_preta, 0.22, 0.65, label='Taxa Raça Preta Geral', linestyles='--', color= 'royalblue' )

adjust_text(texts, force_points=0.2, force_text=0.2,
            expand_points=(1, 1), expand_text=(1, 1),
            arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

plt.legend(fontsize=7, loc=4)

plt.text(0.2, -0.1, "Fonte: https://dadosabertos.tse.jus.br/dataset/candidatos-2022", fontsize=6)

plt.savefig("/dbfs/mnt/datalake/tmp/grupos_partidos_diversidade_tamanho.jpeg", dpi=300, transparent=False)

# COMMAND ----------

colors = (df['cluster'] + 1).tolist()

plt.figure(dpi=300)

plt.scatter(df['PCT_FEMININO'],
            df['PCT_PRETA'],
            s=1.7*100*df['MEDIAN_BEM_CANDIDATO'] / df['MEDIAN_BEM_CANDIDATO'].max(),
            c=colors,
            alpha=0.4)

texts = []

lines = zip(df['PCT_FEMININO'].tolist(),
           df['PCT_PRETA'].tolist(),
           df["SG_PARTIDO"].tolist())

for x, y, s in lines:
    texts.append(plt.text(x, y, s, fontsize=8))
    
plt.grid(True)
plt.suptitle("Grupos de Partidos - Candidatos 2022")
plt.title("Quanto maior a bolha, maior a mediana de valor de bens", fontsize=7)
plt.xlabel("Taxa de Mulheres")
plt.ylabel("Taxa de Raça Preta")
plt.ylim(0,0.42)

plt.vlines( taxa_mulheres, 0, 0.42, label='Taxa Mulheres Geral', linestyles='--', color = 'tomato')
plt.hlines( taxa_preta, 0.22, 0.65, label='Taxa Raça Preta Geral', linestyles='--', color= 'royalblue' )

adjust_text(texts, force_points=0.2, force_text=0.2,
            expand_points=(1, 1), expand_text=(1, 1),
            arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

plt.legend(fontsize=7, loc=4)

plt.text(0.2, -0.1, "Fonte: https://dadosabertos.tse.jus.br/dataset/candidatos-2022", fontsize=6)

plt.savefig("/dbfs/mnt/datalake/tmp/grupos_partidos_diversidade_bens.jpeg", dpi=300, transparent=False)

# COMMAND ----------

data = df.sort_values(by='AVG_BEM_CANDIDATO')

plt.figure(figsize=(8,8))

# Create data
bars = data["SG_PARTIDO"]
x_pos = np.arange(len(bars))

plt.ticklabel_format(style='plain')
sns.barplot(data["SG_PARTIDO"], data['AVG_BEM_CANDIDATO'])

# Rotation of the bar names
plt.xticks(x_pos, bars, rotation=90)
plt.title("Distribuição média de valor dos bens por candidato/partido")
plt.xlabel("Partido")
plt.ylabel("Valor Médio de Bens")

plt.grid(True)
plt.tight_layout()


plt.savefig("/dbfs/mnt/datalake/tmp/grupos_partidos_media_bens.jpeg", dpi=125, transparent=False)

# COMMAND ----------

data = df.sort_values(by='MEDIAN_BEM_CANDIDATO')

plt.figure(figsize=(8,8))

# Create data
bars = data["SG_PARTIDO"]
x_pos = np.arange(len(bars))

plt.ticklabel_format(style='plain')
sns.barplot(data["SG_PARTIDO"], data['MEDIAN_BEM_CANDIDATO'])

# Rotation of the bar names
plt.xticks(x_pos, bars, rotation=90)
plt.title("Distribuição mediana de valor dos bens por candidato/partido")
plt.xlabel("Partido")
plt.ylabel("Valor Mediano de Bens")

plt.grid(True)
plt.tight_layout()

plt.savefig("/dbfs/mnt/datalake/tmp/grupos_partidos_mediana_bens.jpeg", dpi=125, transparent=False)

# COMMAND ----------

df[df['cluster']==5]['SG_PARTIDO'].unique()

# COMMAND ----------

# Grupo 0
# PROS, CIDADANIA, DC, PMB, PSB, PMN, SOLIDARIEDADE, MDB, PDT, PSC, REDE, AGIR, PATRIOTA, AVANTE

# Grupo 1
# PSOL, PSTU

# Grupo 2
# UP

# Grupo 3
# PCO, PCB, PT

# Grupo 4
# REPUBLICANOS, PSDB, UNIÃO, PL, PRTB, PV, PTB, PSD, NOVO, PP, PODE

# Grupo 5
# PC do B
