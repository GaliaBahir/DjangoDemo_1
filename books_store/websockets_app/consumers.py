from time import sleep
import json
import random
from channels.generic.websocket import WebsocketConsumer


class CounterConsumer(WebsocketConsumer):

    # def connect(self):
    #     print("Trying to connect")
    #     # accept the connection
    #     self.accept()
    #     print("Socket is connected")
    #     counter = 0
    #     while True:
    #         data = {
    #             'counter': random.randint(1, 1000)
    #         }

    #         self.send(json.dumps(data))
    #         counter += 1
    #         sleep(1)


    def connect(self):
        # accept the connection
        self.accept()

    def disconnect(self, code):
        # close the connection
        self.close()
        print("Socket disconnected with code", code)
   

    def receive(self, data):
        # the websocket doesn't recieve anything currently from the client
        pass
    
    def send_user(self, event):
        self.send(json.dumps({"ping": "pong"}))


