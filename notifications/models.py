from django.db import models
from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print('Saved Called')
        channel_layer = get_channel_layer()
        notifications_obj = Notifications.objects.filter(is_seen=False).count()
        data = {
            'count': notifications_obj,
            'current_notifications' : self.notification
        }
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group' , {
                'type' : 'send_notification', #Method name Of test_consumer_group group name
                'value' : json.dumps(data)
            }
        )
        super(Notifications, self).save(*args, **kwargs)
