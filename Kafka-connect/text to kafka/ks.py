import ksql

client = ksql.KSQLAPI('http://localhost:8088')

# Create a stream
print(client)