# Databricks notebook source
df= spark.range(0,99).toDF('Numbers')

# COMMAND ----------

df2= spark.range(0,200).toDF('Numbers')

# COMMAND ----------

display(df2)
