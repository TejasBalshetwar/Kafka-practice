from schema_registry.client import SchemaRegistryClient, schema

schema_registry = SchemaRegistryClient(url='http://localhost:8081')

schema = {
    "type": "record",
    "name": "myrecord",
    "fields": [
        {"name": "field1", "type": "string"},
        {"name": "field2", "type": "int"}
    ]
}
print(schema_registry)
# avro_schema = schema.AvroSchema(schema)
schema_registry.register("myrecord",schema=schema)
# schema_id = client.register("test-deployment", avro_schema)