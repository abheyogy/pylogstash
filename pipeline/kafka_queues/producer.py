'''Program to publish data to Kafka topics.'''
from kafka import KafkaProducer


# TODO(Pranav): Move this to a configuration file.
KAFKA_SERVERS = [
        "kfk04.sboxdc.com:9092",
        "kfk05.sboxdc.com:9092",
        "kfk06.sboxdc.com:9092"]

LOCAL_KAFKA_SERVERS = [
        "192.168.1.7:9092"
        ]


def publish_data(data, topic='portkey-newformat'):
    '''Publish data the given Kafka topic.'''

    producer = KafkaProducer(retries=7, bootstrap_servers=KAFKA_SERVERS)
    local_producer = KafkaProducer(retries=7, bootstrap_servers=LOCAL_KAFKA_SERVERS)

    # Asynchronous by default
    for d in data:
        future = producer.send(topic, d.encode('utf-8'))
        local_producer = producer.send('portkey', d.encode('utf-8'))
        producer.flush()

    producer.close()
