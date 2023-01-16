from confluent_kafka import Producer,SerializingProducer
from confluent_kafka.serialization import StringSerializer
from cksr import schema_creation
import os

broker = os.environ.get('KAFKA_BROKER')
avro_serializer = schema_creation()

def producer_with_partition():
    producer = Producer({'bootstrap.servers':broker})
    producer.produce('first',value="partition value",partition=2)
    producer.flush()

def call(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

# producer along with callback and without serializers
def producer_with_callback():
    producer = Producer({'bootstrap.servers': broker})
    producer.produce('first', key="key", value="msg from confluent kafka", callback=call)
    producer.flush()

# producer with serializers
def producer_with_serializer():
    producer = SerializingProducer({'bootstrap.servers': broker,'key.serializer': StringSerializer(),'value.serializer': avro_serializer})
    producer.produce('first', key='serialized_key', value="{ 'name': 'John', 'age': 31 }")
    producer.flush()
    
# producing to a specific partition
def producer_with_partition():
    producer = Producer({'bootstrap.servers': broker})
    producer.produce('first',value="partition value",partition=2)
    producer.flush()

producer_with_serializer()
