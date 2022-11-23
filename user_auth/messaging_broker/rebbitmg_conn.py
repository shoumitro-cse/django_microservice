from pika import URLParameters, BlockingConnection, BasicProperties
from django.conf import settings


class RabbitmqConnection(object):
    conn = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RabbitmqConnection, cls).__new__(cls)
        if not cls.instance.conn:
            print("----Message broker connected---")
            cls.instance.conn = BlockingConnection(URLParameters(settings.REBBITMQ_BROKER_URL))
        return cls.instance

    def get_connection(self):
        return self.conn

    @staticmethod
    def get_channel_connection():
        return RabbitmqConnection().get_connection().channel()
        # return RabbitmqConnection().conn.channel()
