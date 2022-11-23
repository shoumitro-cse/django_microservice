from accounts.consumer_callback import messanger_callback
# from notification.consumer import notification_callback
from messaging_broker.rebbitmg_conn import RabbitmqConnection


class MessageBrokerConsumer:

    # get channel connection
    channel = RabbitmqConnection.get_channel_connection()

    def add_channel_queue(self, queue_key):
        """ add channel queue """
        self.channel.queue_declare(queue=queue_key)

    def add_channel_callback(self, queue_key, callback_fun):
        """ add channel callback function """

        self.channel.basic_consume(queue=queue_key, on_message_callback=callback_fun, auto_ack=True)

    def start_consuming(self):
        print('User auth started consuming...')
        self.channel.start_consuming()

    def stop_consuming(self):
        self.channel.close()

    def restart_consuming(self):
        self.stop_consuming()
        self.start_consuming()


msg_broker_consumer = MessageBrokerConsumer()

msg_broker_consumer.add_channel_queue('user_auth')
msg_broker_consumer.add_channel_callback('user_auth', messanger_callback)

# msg_broker_consumer.add_channel_queue('notification')
# msg_broker_consumer.add_channel_callback('notification', notification_callback)
