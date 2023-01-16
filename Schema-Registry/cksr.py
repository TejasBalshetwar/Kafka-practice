# from confluent_kafka import SerializingProducer
import json
from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
from confluent_kafka.schema_registry.avro import AvroSerializer
import os
schema_registry = SchemaRegistryClient({'url': os.environ.get('SCHEMA_REGISTRY_URL')})

schema = '{"type": "record", "name": "User", "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}]}'
avro_serializer = AvroSerializer(schema_registry_client=schema_registry,schema_str=str(schema))
print(avro_serializer)
