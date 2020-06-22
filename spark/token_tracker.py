from decouple import config
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import explode, concat, col, lit, split, translate, row_number, arrays_zip
from pyspark.sql.types import *
from pyspark.sql.window import Window

PG_SERVER = config('PG_SERVER')
PG_USER = config('PG_USER')
PG_PASSWORD = config('PG_PASSWORD')

spark_context = SparkContext(conf=SparkConf().setAppName("Token Tracker"))

spark = SparkSession \
    .builder \
    .appName("Token Tracker") \
    .config("spark.jars", "/path_to_postgresDriver/postgresql-42.2.5.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", f"jdbc:postgresql://{PG_SERVER}") \
    .option("dbtable", "token_transfers_test") \
    .option("user", PG_USER) \
    .option("password", PG_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

df_dai = df.filter(df["token_address"] == "0x6b175474e89094c44da98b954eedeac495271d0f")

spark.stop()
