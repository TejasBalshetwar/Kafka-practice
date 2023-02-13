from confluent_kafka import Producer, SerializingProducer
from confluent_kafka.serialization import StringSerializer
import confluent_kafka
import os,time

broker = os.environ.get("KAFKA_BROKER")


def call(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))

conf = {
    "bootstrap.servers": broker,
    "key.serializer": StringSerializer(),
    "value.serializer": StringSerializer(),
    "transactional.id": "my-transactional-id",
    "enable.idempotence":True,
    "acks":"all"
}

producer = SerializingProducer(conf)
producer.init_transactions()
producer.begin_transaction()
for i in range(1091,1110):
    time.sleep(2)
    producer.produce(
        "first",
        key="serialized_key",
        value=f" 'name': 'John', 'age': {i} ",
        on_delivery=call,
    )
    producer.flush()

producer.commit_transaction()

