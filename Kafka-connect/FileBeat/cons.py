from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'logstash-0',
        bootstrap_servers=['localhost:9093'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        group_id='my-group',
)

for message in consumer:
    offset = message.offset
    message = message.value
    print('{}'.format(message.decode('utf-8')))
    print(f"{offset} added")