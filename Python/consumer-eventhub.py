from confluent_kafka import Consumer, KafkaError

# ----------------------------
# Consumer configuration
# ----------------------------
consumer_conf = {
    'bootstrap.servers': "<server_name>:9093", # Event Hub Server name
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'sasl.password': "<Connection_String>", # Primary connection string
    'ssl.endpoint.identification.algorithm': 'https',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

eventhub_name = "test" # Topic name

consumer = Consumer(consumer_conf)
consumer.subscribe([eventhub_name])

print("Consuming messages...")
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                print(f"Consumer error: {msg.error()}")
            continue
        print(f"Received message: {msg.key().decode('utf-8')} -> {msg.value().decode('utf-8')} from Event Hub: {msg.topic()}")
except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    consumer.close()