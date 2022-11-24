import json
from pika import BasicProperties
from messaging_broker.rebbitmg_conn import RabbitmqConnection


def push_sms(method, event_data):
    channel = RabbitmqConnection.get_channel_connection()
    properties = BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='company',
        body=json.dumps(event_data),
        properties=properties
    )
