import time
import requests
from kafka import KafkaProducer

KAFKA_TOPIC = config('KAFKA_TOPIC1'))
KAFKA_SERVER = config('KAFKA_SERVER')

topic = KAFKA_TOPIC
broker = KAFKA_SERVER
producer = KafkaProducer(bootstrap_servers = broker)
print('Start sending messages')

def follow(thefile):
    thefile.seek(0,2)
    #line_count = 0
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        #line_count += 1
        yield line
        #print(line_count)

if __name__ == '__main__':
    logfile = open("blocks_file.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        #print(line)
        line_stripped = line.rstrip()
        producer.send(topic, line_stripped.encode())
        print("Block message sent to producer.")
