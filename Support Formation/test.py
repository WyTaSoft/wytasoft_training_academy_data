
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import when, col, lit
# Données de transactions
transactions = [
    {"id": 1, "montant": 500, "carte": "crédit", "pays": "US", "heure": "10:00"},
    {"id": 2, "montant": 2000, "carte": "débit", "pays": "FR", "heure": "15:30"},
    {"id": 3, "montant": 1500, "carte": "crédit", "pays": "IN", "heure": "11:00"},
    {"id": 4, "montant": 300, "carte": "débit", "pays": "US", "heure": "09:45"}
]

transaction_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("montant", IntegerType(), True),
    StructField("carte", StringType(), True),
    StructField("pays", StringType(), True),
    StructField("heure", StringType(), True)
])

transactions_df = spark.createDataFrame(transactions, schema=transaction_schema)