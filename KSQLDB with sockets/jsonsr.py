from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import os
import time
broker = os.environ.get('KAFKA_BROKER')
schema_registry = SchemaRegistryClient({'url': "http://schema-registry:8081"})
# schema_str = """{"type":"object","title":"abcd","properties":{"TIMESTAMP":{"type":"string"},"LEVEL":{"type":"string"},"MESSAGE":{"type":"string"}}}"""
schema = schema_registry.get_schema(1)
json_serializer = JSONSerializer(schema_registry_client =schema_registry,schema_str=schema.schema_str)

producer_conf = {'bootstrap.servers': broker,
                    'key.serializer': StringSerializer('utf_8'),
                    'value.serializer': json_serializer}

producer = SerializingProducer(producer_conf)
i=18
producer.produce(topic="log", key="key", value={"TIMESTAMP": "12/11/2022", "LEVEL": "INFO", "MESSAGE": f"Project going on {i}"})
producer.flush()
# for i in range(10):
#     time.sleep(1)
#     producer.produce(topic="log", key="key", value={"TIMESTAMP": "12/11/2022", "LEVEL": "INFO", "MESSAGE": f"Project going on {i}"})
#     producer.flush()

