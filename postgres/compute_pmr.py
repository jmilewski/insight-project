from decouple import config
import numpy as np
import psycopg2
import time

PG_USER = config('PG_USER')
PG_DBNAME = config('PG_DBNAME')
PG_PASSWORD = config('PG_PASSWORD')

conn = psycopg2.connect(f"host=localhost dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWORD}")
cur = conn.cursor()

def price_metcalfe_compute_insert():
    cur.execute("SELECT AVG(price) FROM (SELECT price, timestamp, side FROM iex_events_test WHERE side = 'bid' ORDER BY timestamp DESC LIMIT 10) AS foo;")
    price_decimal = cur.fetchone()
    price = float(price_decimal[0])
    cur.execute("SELECT AVG(transaction_count) FROM (SELECT transaction_count, timestamp FROM blocks_test ORDER BY timestamp DESC LIMIT 20) AS foo;")
    transaction_count_decimal = cur.fetchone()
    transaction_count = float(transaction_count_decimal[0])
    transaction_count_extrapolated = transaction_count * 6300
    token_supply = 111000000
    price_metcalfe_ratio = np.log( price / (100*(transaction_count_extrapolated**1.5/token_supply)) )
    timestamp = int(round(time.time()*1000))
    values = [timestamp, price_metcalfe_ratio]
    cur.execute("INSERT INTO price_metcalfe_ratio VALUES (%s, %s)", values)
    conn.commit()

while True:
    price_metcalfe_compute_insert()
    time.sleep(3)
