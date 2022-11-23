from pika import URLParameters, BlockingConnection, BasicProperties
from django.conf import settings


def get_channel_connection():
    params = URLParameters(settings.REBBITMQ_BROKER_URL)
    conn = BlockingConnection(params)
    return conn.channel()
