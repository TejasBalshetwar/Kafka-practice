from confluent_kafka import Consumer,DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
import os,multiprocessing
import time

broker = os.environ.get('KAFKA_BROKER')

conf = {'bootstrap.servers': broker,
        'group.id': "pehla",
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}


def cons():
    conf['key.deserializer'] = StringDeserializer()
    conf["value.deserializer"] = StringDeserializer()
    consumer = DeserializingConsumer(conf)
    consumer.subscribe(['first'])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
            time.sleep(4)
        print(f'Received message: {msg.value()} {msg.topic()} {msg.partition()} {os.getpid()}')

p1 = multiprocessing.Process(target=cons)
p2 = multiprocessing.Process(target=cons)
p3 = multiprocessing.Process(target=cons)

if __name__=="__main__":
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()