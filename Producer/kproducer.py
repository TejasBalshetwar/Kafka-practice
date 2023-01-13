from kafka import  KafkaProducer
import json

# specify the partition to send the message to
def producer_with_partition_specified():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('first', value='my message', key=None, partition=2)
    producer.flush()

# send the message with key
def producer_with_keys():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('first', key=b'key1', value=b'value1')
    producer.send('first', key=b'key2', value=b'value2')
    producer.flush()

# serializing the vlaue
def producer_value_serializer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('first', 'this is a serilized message')
    producer.flush()

# serializing the key
def producer_key_serializer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',key_serializer=str.encode)
    producer.send('first', key='key', value=b'1234')

# serializing the key and value
def producer_with_key_and_value_serializer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092',key_serializer=str.encode, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send('first', key='key', value='{ "name": "John", "age": 30 }')
    print("sent")

# callback function
def on_send(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def msg_with_callback():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('first', b'raw_bytes').add_callback(on_send)

producer_with_key_and_value_serializer()