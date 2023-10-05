# Databricks notebook source
df= spark.range(0,100).toDF('Numbers')

# COMMAND ----------

display(df)
