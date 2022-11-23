import json
from pika import BasicProperties
from messaging_broker.rebbitmg_conn import get_channel_connection

channel = get_channel_connection()


def push_sms(method, event_data):
    properties = BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='company',
        body=json.dumps(event_data),
        properties=properties
    )
