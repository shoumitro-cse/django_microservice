from pika import URLParameters, BlockingConnection, BasicProperties
from django.conf import settings


class RabbitmqConnection(object):
    conn = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RabbitmqConnection, cls).__new__(cls)
            cls.instance.conn = BlockingConnection(URLParameters(settings.REBBITMQ_BROKER_URL))
            print("----Message broker connected---")
        return cls.instance

    def get_connection(self):
        return self.conn

    @staticmethod
    def get_channel_connection():
        return RabbitmqConnection().get_connection().channel()
        # return RabbitmqConnection().conn.channel()
