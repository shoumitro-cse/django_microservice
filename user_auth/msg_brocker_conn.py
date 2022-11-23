import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_auth.settings')
django.setup()
from messaging_broker.consumer import channel


while(True):
	try:
		print('User auth started consuming...')
		channel.start_consuming()
	except Exception as e:
		pass
