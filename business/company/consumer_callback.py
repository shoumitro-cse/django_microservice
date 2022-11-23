import json
from django.utils import timezone
import logging
logger = logging.getLogger(__name__)


def messanger_callback(ch, method, properties, body):
    try:
        data_list = json.loads(body)
        print("data_list: ", data_list)
    except Exception as e:
        logger.debug(e)

