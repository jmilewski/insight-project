from os.path import abspath
from decouple import config
import pyspark.sql.functions as f
from pyspark.sql.types import ArrayType, StringType
from pyspark.sql import SparkSession

PG_USER = config('PG_USER')
PG_DBNAME = config('PG_DBNAME')
PG_PASSWORD = config('PG_PASSWORD')
PG_SERVER = config('PG_SERVER')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.jars", "/path_to_postgresDriver/postgresql-42.2.5.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", f"jdbc:postgresql://{PG_SERVER}/{PG_DBNAME}") \
    .option("dbtable", "token_transfers_test") \
    .option("user", PG_USER) \
    .option("password", PG_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

def dai_sum_by_block():
    df_dai = df.filter(df["token_address"]=="0x6b175474e89094c44da98b954eedeac495271d0f")
    df_dai_by_block = df_dai.select("block_number","value").groupBy("block_number").sum("value")
