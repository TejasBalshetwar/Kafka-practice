def schema_creation():
    from confluent_kafka.schema_registry.schema_registry_client import SchemaRegistryClient 
    from confluent_kafka.schema_registry.avro import AvroSerializer
    schema_registry = SchemaRegistryClient({"url":"http://localhost:8081"})
    schema = '{"type": "record", "name": "User", "fields": [{"name": "name", "type": "string"}, {"name": "age", "type": "int"}]}'
    avro_serializer = AvroSerializer(schema_registry_client=schema_registry,schema_str=str(schema))
    return avro_serializer