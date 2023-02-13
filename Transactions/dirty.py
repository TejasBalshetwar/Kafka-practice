from confluent_kafka import Consumer,DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
import os,multiprocessing
import time

broker = os.environ.get('KAFKA_BROKER')

conf = {'bootstrap.servers': broker,
        'group.id': "qdsfjsduhfiuersdxtfyhj21312",
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,}


# without isolation level
def cons2():
    conf['key.deserializer'] = StringDeserializer()
    conf["value.deserializer"] = StringDeserializer()
    conf["isolation.level"]="read_uncommitted"
    consumer = DeserializingConsumer(conf)
    consumer.subscribe(['first'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        print(f'Received message: {msg.value()} in dirty read')


cons2()
