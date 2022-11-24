import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business.settings')
django.setup()

from messaging_broker.consumer import msg_broker_consumer

if msg_broker_consumer.channel:
    msg_broker_consumer.start_consuming()
