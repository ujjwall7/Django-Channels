from django.shortcuts import render

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time

async def home(request):
    
    for i in range(1, 10+1):
        channel_layer = get_channel_layer()
        data = {'count' : i}
        await (channel_layer.group_send)(
            'new_consumer_group' , {
                'type' : 'send_notification', #Method name Of test_consumer_group group name
                'value' : json.dumps(data)
            }
        )
        time.sleep(i)
    return render(request, "home.html")





