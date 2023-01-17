from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import os

broker = os.environ.get('KAFKA_BROKER')
schema_registry = SchemaRegistryClient({'url': "http://schemaregistry:8081"})
schema_str = """{"type":"object","title":"abcd","properties":{"f1":{"type":"string"}}}"""

json_serializer = JSONSerializer(schema_registry_client =schema_registry,schema_str=schema_str)

producer_conf = {'bootstrap.servers': broker,
                    'key.serializer': StringSerializer('utf_8'),
                    'value.serializer': json_serializer}

producer = SerializingProducer(producer_conf)

producer.produce(topic="first", key="key", value={"f1": "value4"})
producer.flush()

