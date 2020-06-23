from os.path import abspath
from decouple import config
import pyspark.sql.functions as f
from pyspark.sql.types import ArrayType, StringType
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.jars", "/path_to_postgresDriver/postgresql-42.2.5.jar") \
    .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://10.0.0.5:5432/postgres") \
    .option("dbtable", "token_transfers_test") \
    .option("user", "db_select") \
    .option("password", "<setpassword>") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df_dai = df.filter(df["token_address"]=="0x6b175474e89094c44da98b954eedeac495271d0f")

df_dai.count()

dai_value_transferred = df_dai.groupBy("token_address").sum().collect()[0][1]
