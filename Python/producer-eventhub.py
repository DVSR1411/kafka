from confluent_kafka import Producer

# ----------------------------
# Producer configuration
# ----------------------------
producer_conf = {
    'bootstrap.servers': "<server_name>:9093", # Event Hub Server name
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'sasl.password': "<Connection_String>",
    'ssl.endpoint.identification.algorithm': 'https',
    'acks': 'all'
}

eventhub_name = "test" #Topic name

producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce some test messages
for i in range(1,10):
    producer.produce(eventhub_name, key=f"key{i}", value="Hello from Python!", callback=delivery_report)
    producer.flush()