# 📊 Análise Exploratória com PySpark - Camada Bronze (Dummy Data)
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Simulando a leitura da tabela bronze de leads (dados dummy)
df = spark.table("default.tb_leads_dummy_bronze")  # Substituído schema real por 'default'

# 🔍 Exemplo de Lazy Evaluation
df_lazy = df.filter(col("lead_status") == 'CONTACTED') \
    .select("lead_opportunity_id", "lead_status", "lead_open_dt") \
    .withColumnRenamed("lead_status", "status") \
    .withColumnRenamed("lead_open_dt", "open_date")

print("Transformações aplicadas sem execução ainda.")
display(df_lazy.limit(10))

# 🧾 Estrutura da tabela
df.printSchema()
display(df.limit(10))

# 📈 Contagem total de registros
print("Total de registros:", df.count())

# 📊 Contagem de valores por lead_status
df.select("lead_status").distinct().display()
df.groupBy("lead_status").count().orderBy(col("count").desc()).display()

# 🔁 Verificação de duplicatas
df.groupBy("lead_opportunity_id").count().filter(col("count") > 1).orderBy(col("count").desc()).display()

# 🧹 Remoção de duplicatas simples
df_dedup = df.dropDuplicates(["lead_opportunity_id"])
print("Antes:", df.count(), " | Depois:", df_dedup.count())

# 🧼 Removendo duplicatas mantendo o mais recente
window = Window.partitionBy("lead_opportunity_id").orderBy(col("etl_med_timestamp").desc(), col("etl_timestamp").desc())

df_ranked = df.withColumn("row_num", row_number().over(window))
df_dedup_latest = df_ranked.filter(col("row_num") == 1).drop("row_num")

print("Antes:", df.count(), " | Depois:", df_dedup_latest.count())
display(df_dedup_latest.limit(10))

# 🧮 Contagem aproximada de valores únicos por coluna
df.select([
    approx_count_distinct(col(c)).alias(f"{c}_unique_values")
    for c in df.columns
]).display()
