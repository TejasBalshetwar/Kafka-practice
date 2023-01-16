from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "192.168.1.105:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
def producer_with_key_callback():
    producer.produce('my-topic', key="key", value="msg from confluent kafka", callback=acked)
    producer.flush()
    producer.poll(1)

producer_with_key_callback()