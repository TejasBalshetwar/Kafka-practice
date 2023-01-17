from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
import os

broker = os.environ.get('KAFKA_BROKER')
schema_registry = SchemaRegistryClient({'url': "http://schemaregistry:8081"})
# print(schema_registry)
schema = '{"type": "record", "name": "User", "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}]}'
avro_serializer = AvroSerializer(schema_registry_client=schema_registry, schema_str=schema)

conf = {'bootstrap.servers': broker,'key.serializer': StringSerializer(),'value.serializer': avro_serializer}
producer = SerializingProducer(conf)
def call(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce(topic='second', key='key', value={"name": "sanskar", "age": 25000},on_delivery=call)
producer.flush()
