from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka import DeserializingConsumer
from confluent_kafka.serialization import StringDeserializer
import os

broker = os.environ.get('KAFKA_BROKER')
schema_registry = SchemaRegistryClient({'url': "http://schemaregistry:8081"})
schema = schema_registry.get_schema(1)

avro_deserializer = AvroDeserializer(schema_registry_client=schema_registry, schema_str=schema.schema_str)

conf = {'bootstrap.servers': broker,'key.deserializer': StringDeserializer('utf_8'),'value.deserializer': avro_deserializer,'group.id': "mygroup",'auto.offset.reset': 'earliest','enable.auto.commit': False}
consumer = DeserializingConsumer(conf)

consumer.subscribe(['second'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print('Received message: {}'.format(msg.value()))
