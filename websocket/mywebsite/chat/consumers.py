import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are noe connected!'
        }))
         

    # def receive(self,text_data):
    #     pass


    # def disconnect():
    #     pass