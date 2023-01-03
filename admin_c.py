from kafka.admin import KafkaAdminClient,NewTopic,NewPartitions

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

topic_list = []

topic_list.append(NewTopic(name="first", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="second", num_partitions=2, replication_factor=1))
topic_list.append(NewTopic(name="third", num_partitions=3, replication_factor=1))

# Creating topics
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

# describing topics
print(admin_client.describe_topics(topics=["first"]))

# deleting topics
# admin_client.delete_topics(topics=["third"])

# listing topics
print(admin_client.list_topics())

# creating partitions
admin_client.create_partitions(topic_partitions={"first": NewPartitions(total_count=4)})

# using the confluent-kafka library'
# from confluent_kafka.admin import AdminClient, NewTopic

# admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
# topic_list = []
# topic_list.append(NewTopic("first", num_partitions=1, replication_factor=1))
# topic_list.append(NewTopic("second", num_partitions=2, replication_factor=1))
# topic_list.append(NewTopic("third", num_partitions=3, replication_factor=1))

# Creating topics
# admin_client.create_topics(new_topics=topic_list)

# describing topics
# print(admin_client.list_topics())

# deleting topics
# admin_client.delete_topics(topics=["third"])

# listing topics
# print(admin_client.list_topics())

# creating partitions
# admin_client.create_partitions(topic_partitions={"first": NewPartitions(total_count=4)})

# change replication factor
# admin_client.create_partitions(topic_partitions={"first": NewPartitions(total_count=4, replication_factor=2)})
