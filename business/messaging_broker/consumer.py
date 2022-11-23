from company.consumer_callback import messanger_callback
# from notification.consumer import notification_callback
from messaging_broker.rebbitmg_conn import get_channel_connection


# get channel connection
channel = get_channel_connection()

# add channel queue
channel.queue_declare(queue='company')
# channel.queue_declare(queue='notification')

# add channel callback function
channel.basic_consume(queue='company', on_message_callback=messanger_callback, auto_ack=True)
# channel.basic_consume(queue='notification', on_message_callback=notification_callback, auto_ack=True)

