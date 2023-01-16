from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer
import os
broker = os.environ.get('KAFKA_BROKER')
print(broker)

def producer_with_partition():
    producer = Producer({'bootstrap.servers':broker})
    producer.produce('first',value="partition value",partition=2)
    producer.flush()

def call(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

# async producer along with callback
def producer_with_callback():
    producer = Producer({'bootstrap.servers': broker})
    producer.produce('first', key="key", value="msg from confluent kafka", callback=call)
    producer.poll(1)

# sync producer with serializers
def producer_with_serializer():
    producer = Producer({'bootstrap.servers': broker})
    producer.set_key_serializer(StringSerializer())
    producer.set_value_serializer(JSONSerializer())
    producer.produce('first', key='serialized_key', value="{ 'name': 'John', 'age': 30 }")
    producer.flush()


producer_with_serializer()
