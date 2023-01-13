from kafka import KafkaConsumer,TopicPartition
import json

def consumer_with_earliest():
    consumer = KafkaConsumer('first', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=False, group_id='my-group-1')
    for message in consumer:
        print(message.value)

def consumer_with_latest():
    consumer = KafkaConsumer('first', bootstrap_servers=['localhost:9092'], auto_offset_reset='latest', enable_auto_commit=False, group_id='my-group-2')
    for message in consumer:
        print(message.value)

def consumer_with_some_offset():
    consumer = KafkaConsumer('first', bootstrap_servers=['localhost:9092'], enable_auto_commit=False, group_id='my-group-3')
    # consumer.beginning_offsets([TopicPartition('first', 0)]) getting first offset of specific partition
    # consumer.seek_to_beginning() go ti beginning offset

    # using first topic and 0th partition
    consumer.assign([TopicPartition('first', 0)])
    for message in consumer:
        print(message.value)
    
def consumer_deserialisers():
    consumer = KafkaConsumer('first', bootstrap_servers=['localhost:9092'], enable_auto_commit=False, group_id='my-group-4', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    for message in consumer:
        print(message.value)
     
def commiting():
    consumer = KafkaConsumer('first', bootstrap_servers=['localhost:9092'], enable_auto_commit=False, group_id='my-group-5')
    for message in consumer:
        print(message.value)
        consumer.commit()
    
if __name__=="__main__":
    commiting()