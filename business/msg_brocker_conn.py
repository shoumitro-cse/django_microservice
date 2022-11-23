import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'business.settings')
django.setup()
from messaging_broker.consumer import channel


while(True):
	try:
		print('Started Consuming...')
		channel.start_consuming()
	except Exception as e:
		pass
