from decouple import config
import psycopg2
import json
from kafka import KafkaConsumer

PG_USER = config('PG_USER')
PG_DBNAME = config('PG_DBNAME')
PG_PASSWORD = config('PG_PASSWORD')

conn = psycopg2.connect(f"host=localhost dbname={PG_DBNAME} user={PG_USER} password={PG_PASSWORD}")
cur = conn.cursor()

# Consume latest messages and auto-commit offsets
consumer = KafkaConsumer('node-blocks-test7', group_id='test-group', bootstrap_servers=['10.0.0.14:9092'])

for message in consumer:
    if message.value:
        try:
            print(message.value)
            decoded_message = message.value.decode('utf-8').rstrip()
            decoded_message_dict = json.loads(decoded_message)
            values = []
            for key in decoded_message_dict:
                values.append(str(decoded_message_dict[key]))
            cur.execute("INSERT INTO blocks_test VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)
            conn.commit()
        except json.decoder.JSONDecodeError:
            print("JSON Decode Error")

#conn.close()
