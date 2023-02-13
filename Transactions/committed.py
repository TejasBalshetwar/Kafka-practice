from confluent_kafka import Consumer,DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
import os,multiprocessing
import time

broker = os.environ.get('KAFKA_BROKER')

conf = {'bootstrap.servers': broker,
        'group.id': "qdsfjsduhfiuersdxtfyhjdfvfdb",
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,}

def cons():
    conf['key.deserializer'] = StringDeserializer()
    conf["value.deserializer"] = StringDeserializer()
    conf["isolation.level"]="read_committed"
    consumer = DeserializingConsumer(conf)
    consumer.subscribe(['first'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print(f'Received message: {msg.value()} in read committed')
    
cons()