# Databricks notebook source
# MAGIC %pip install bokeh adjustText

# COMMAND ----------

from sklearn import cluster
from bokeh.plotting import figure, output_file, save
from bokeh.io import show
import matplotlib.pyplot as plt

from adjustText import adjust_text

df = spark.table("silver_tse.sumario_partido").toPandas()

# COMMAND ----------

# DBTITLE 1,Clusters Partidos
features = ['PCT_FEMININO','PCT_PRETA']

model = cluster.KMeans(n_clusters=6)

model.fit(df[features])
df['cluster'] = model.labels_

# COMMAND ----------

df_cluster = df.groupby('cluster')[features].mean().reset_index()
df_cluster = df_cluster.merge( df.groupby('cluster')[['SG_PARTIDO']].count().reset_index() )
df_cluster

# COMMAND ----------

for c in df['cluster'].unique():
    data = df[df['cluster']==c]
    partidos = data['SG_PARTIDO']
    tx_fem = data['PCT_FEMININO']
    tx_preta = data['PCT_PRETA']
    plt.plot(tx_fem, tx_preta, 'o')

texts = []
for x, y, s in zip(df['PCT_FEMININO'].tolist(),
                   df['PCT_PRETA'].tolist(),
                   df["SG_PARTIDO"].tolist()):
    texts.append(plt.text(x, y, s, fontsize=8))
    
plt.grid(True)
plt.title("Grupos de Partidos")
plt.xlabel("Taxa de Mulheres")
plt.ylabel("Taxa de Raça Preta")
plt.ylim(0,0.42)

plt.vlines( df['PCT_FEMININO'].mean(), 0, 0.42, label='Taxa média de Mulheres', linestyles='--', color = 'tomato')
plt.hlines( df['PCT_PRETA'].mean(), 0.22, 0.65, label='Taxa média de Raça Preta', linestyles='--', color= 'royalblue' )

adjust_text(texts, force_points=0.2, force_text=0.2,
            expand_points=(1, 1), expand_text=(1, 1),
            arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

plt.legend(fontsize=7, loc=4)

plt.savefig("/dbfs/mnt/datalake/raw/grupos_partidos_diversidade.jpeg", dpi=300, transparent=False)

# COMMAND ----------


