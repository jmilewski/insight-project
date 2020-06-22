from decouple import config
import requests
from kafka import KafkaProducer

IEX_API_TOKEN = config('IEX_API_TOKEN')

topic = 'iex-events-test'
broker = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers = broker)
print('Start sending messages')

r = requests.get(f'https://cloud-sse.iexapis.com/stable/cryptoEvents?symbols=ethusd&token={IEX_API_TOKEN}', stream=True)

for line in r.iter_lines():
    if line:
        decoded_line = line.decode('utf-8')
        if decoded_line == 'data: []':
            print('No data on that line.')
        else:
            decoded_line_spliced = decoded_line[7:-1]
            producer.send(topic, decoded_line_spliced.encode())
            print("Event message sent to producer.")
