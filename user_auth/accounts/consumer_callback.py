import json
from django.utils import timezone
import logging
logger = logging.getLogger(__name__)
from accounts.models import User
from accounts.producer import push_sms


def messanger_callback(ch, method, properties, body):
    try:
        data_list = json.loads(body)
        print("data_list: ", data_list)
        user = User.objects.get(id=data_list.get("pk"))
        user.jwt_secret = "hello"
        push_sms("jwt_secret", {"data": f"{user.pk} jwt_secret updated."})
    except Exception as e:
        logger.debug(e)

