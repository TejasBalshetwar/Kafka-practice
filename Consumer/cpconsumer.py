from confluent_kafka import Consumer, KafkaError
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group-5',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['first'])
