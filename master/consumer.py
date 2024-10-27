#State bni raiti hai -> connection orinted -> yaad rakhta hai
 
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json



class TestConsumer(WebsocketConsumer):
    
    # ws://
    def connect(self):
        print('==============Started================')
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name, 
        )
        self.accept()
        self.send(text_data = json.dumps({'status' : 'connected'})) # json.dumps is used for json convert to string


    def receive(self, text_data):
        print(f"{text_data = }")
        self.send(text_data=json.dumps({
            'status' : True,
            'msg' : 'Got Your Data'
        }))
        # pass

    def disconnect(self, *args, **kwargs):
        print('===========Disconnected===========')
        pass

    def send_notification(self, event):
        print('===============Send Notification===============')
        # print(event)
        print(event.get('value'))
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))
        print("===============Ended===============")











