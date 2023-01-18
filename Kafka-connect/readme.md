# CSV to Kafka and Kafka to Postgres 
The connectors used would be SpoolDirCsvSourceConnector and JdbcSinkConnector

Step 1:
Run the docker-compose file 

docker-compose up

Step 2:
Check all available connector-plugins

curl http://localhost:8083/connector-plugins

Step 3:
Create a csv to kafka connector using the below command:

curl -i -X PUT -H "Accept:application/json" \
    -H  "Content-Type:application/json" http://localhost:8083/connectors/source-csv-spooldir-02/config \
    -d '{
        "connector.class": "com.github.jcustenborder.kafka.connect.spooldir.SpoolDirCsvSourceConnector",
        "topic": "orders_spooldir_02",
        "input.path": "/data/unprocessed",
        "finished.path": "/data/processed",
        "error.path": "/data/error",
        "input.file.pattern": ".*\\.csv",
        "schema.generation.enabled":"true",
        "schema.generation.key.fields":"order_id",
        "csv.first.row.as.header":"true",
        "transforms":"castTypes",
        "transforms.castTypes.type":"org.apache.kafka.connect.transforms.Cast$Value",
        "transforms.castTypes.spec":"order_id:int32,customer_id:int32,order_total_usd:float32"
        }'

### Information about the config: https://docs.confluent.io/kafka-connectors/spooldir/current/connectors/csv_source_connector.html#csv-parsing
The above command creates a connector which is SpoolDirCsvSourceConnector with auto schema generation and some single message transforms for type casting(if not used then string type will be assigned to all elements).

Step 4:
Check if data reached in kafka using a simple consumer(don't forget to deserialise using the schema generated).

Step 5:
Create a connector for kafka to postgres using the below command:

curl -X PUT http://localhost:8083/connectors/sink-postgres-orders-00/config \
    -H "Content-Type: application/json" \
    -d '{
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "connection.url": "jdbc:postgresql://postgres:5432/",
        "connection.user": "postgres",
        "connection.password": "postgres",
        "tasks.max": "1",
        "topics": "orders_spooldir_02",
        "auto.create": "true",
        "auto.evolve":"true",
        "pk.mode":"record_value",
        "pk.fields":"order_id",
        "insert.mode": "upsert",
        "table.name.format":"orders"
    }'

### Information about the config: https://docs.confluent.io/kafka-connectors/jdbc/current/sink-connector/sink_config_options.html#writes
The above command creates a connector which sends data from kafka to the specified postgres database and uses the schema to create the table if it's not present and use order_id as primary key and the insert mode is upsert which means while inserting check if order with same order_id exists and if so update that. 

The table is created and if you supply any other file to csv connector it will automatically add those contents to kafka and the jdbc sink connector will add those contents to the table. This is very low latency process which can be considered to be almost "real-time".