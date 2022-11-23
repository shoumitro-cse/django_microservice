from pika import URLParameters, BlockingConnection, BasicProperties
from django.conf import settings


class RabbitmqConnection(object):
    conn = None

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(RabbitmqConnection, cls).__new__(cls)
    #     return cls.instance

    def __init__(self):
        if not self.conn:
            params = URLParameters(settings.REBBITMQ_BROKER_URL)
            self.conn = BlockingConnection(params)

    def get_connection(self):
        return self.conn

    @staticmethod
    def get_channel_connection():
        conn = RabbitmqConnection().get_connection()
        return conn.channel()
