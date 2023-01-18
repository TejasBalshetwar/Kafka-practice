from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
# from confluent_kafka.schema_registry import SchemaRegistryClient


admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = []
print(admin_client.list_topics())
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=False, group_id='my-grou1')
consumer.subscribe(['orders_spooldir_01'])
for message in consumer:
    print (message.value)