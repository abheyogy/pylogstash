'''Program to consume Kafka topics and fetch topic data.'''
from kafka import KafkaConsumer


# TODO(Pranav): Move this to a configuration file.
KAFKA_SERVERS = [
        "kfk04.sboxdc.com:9092",
        "kfk05.sboxdc.com:9092",
        "kfk06.sboxdc.com:9092"]
MESSAGES = []


def consume_topics(topic='portkey'):
    '''Consume data from a given topic in Kafka.'''

    # Consume PortKey data from Kafka
    consumer = KafkaConsumer(topic,
                             client_id='pylogpipe',
                             group_id='mon_pipeline_test',
                             enable_auto_commit=True,
                             bootstrap_servers=KAFKA_SERVERS)

    def _consume_msgs():
        '''Wrapper function for consuming messages from Kafka.'''
        counter = 0
        for message in consumer:

            MESSAGES.append(message.value.decode('utf-8'))
            # TODO(Pranav): There should be a better way. Maybe consumer.poll()?
            counter += 1
            if counter > 7:
                break

    try:
        _consume_msgs()
    except Exception as ex:
        print("Exception @Kafka Consumer:", ex)

    consumer.close()
    return MESSAGES


if __name__ == '__main__':
    print(consume_topics())
