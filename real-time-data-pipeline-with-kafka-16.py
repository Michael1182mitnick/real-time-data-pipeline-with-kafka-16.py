# Real Time Date Pipeline with Kafka
# pip install kafka-python
# Set up a real-time data pipeline using Apache Kafka to ingest, process, and analyze streaming data from multiple sources.
# Start Zookeeper on port 2181
# bin/zookeeper-server-start.sh config/zookeeper.properties
# Start Kafka on port 9092
# bin/kafka-server-start.sh config/server.properties
# Set Up Kafka Topics
# Create a Kafka topic called 'streaming-data'
# bin/kafka-topics.sh --create --topic streaming-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
# You can check the created topic using:
# bin/kafka-topics.sh --list --bootstrap-server localhost:9092

from kafka import KafkaProducer
import json
import time
import random

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulate real-time data ingestion


def send_data():
    for i in range(100):
        data = {
            'sensor_id': f'sensor_{random.randint(1, 5)}',
            'temperature': random.uniform(20.0, 100.0),
            'timestamp': time.time()
        }
        print(f"Sending data: {data}")
        producer.send('streaming-data', value=data)
        time.sleep(2)  # Simulate delay between data points


if __name__ == "__main__":
    send_data()
