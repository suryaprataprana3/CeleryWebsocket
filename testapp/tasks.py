# from celery.decorators import task
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from asgiref.sync import async_to_sync
from .models import *
import time
import logging
log = logging.getLogger('yourapp')


@shared_task
def go_to_sleep_and_show(room_name,message):
    Chats.objects.create(chats=message)
    time.sleep(2)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        room_name,
        {
                'type': 'chat_message',
                'message': "how are you?"
        }
    )
    return True