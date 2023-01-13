from confluent_kafka.admin import AdminClient, NewTopic, NewPartitions

admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
topic_list = []
topic_list.append(NewTopic("fourth", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic("fifth", num_partitions=2, replication_factor=1))
topic_list.append(NewTopic("sixth", num_partitions=3, replication_factor=1))

# Creating topics
admin_client.create_topics(new_topics=topic_list)

# describing topics
print(admin_client.list_topics())

# deleting topics
admin_client.delete_topics(topics=["third"])

# listing topics
print(admin_client.list_topics())

# creating partitions
admin_client.create_partitions(topic_partitions={"first": NewPartitions(total_count=4)})
