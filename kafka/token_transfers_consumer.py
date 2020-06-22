from decouple import config
import psycopg2
import json
from kafka import KafkaConsumer

PG_USER = config('PG_USER')
PG_DBNAME = config('PG_DBNAME')
PG_PASSWORD = config('PG_PASSWORD')
KAFKA_TOPIC = config('KAFKA_TOPIC3')
KAFKA_GROUPID = config('KAFKA_GROUPID')
KAFKA_SERVER = config('KAFKA_SERVER')

conn = psycopg2.connect(f"host=localhost dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWORD}")
cur = conn.cursor()

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(KAFKA_TOPIC, group_id=KAFKA_GROUPID, bootstrap_servers=[KAFKA_SERVER])

for message in consumer:
    if message.value:
        try:
            print(message.value)
            decoded_message = message.value.decode('utf-8').rstrip()
            decoded_message_dict = json.loads(decoded_message)
            values = []
            for key in decoded_message_dict:
                values.append(str(decoded_message_dict[key]))
            cur.execute("INSERT INTO token_transfers_test VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)
            conn.commit()
        except json.decoder.JSONDecodeError:
            print("JSON Decode Error")

#conn.close()
