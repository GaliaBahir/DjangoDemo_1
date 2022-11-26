from time import sleep
import json
import random
from channels.generic.websocket import JsonWebsocketConsumer


class CounterConsumer(JsonWebsocketConsumer):

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
        print("Socket is connected")
        
        #await self.send({'text':"hi there"})

    def disconnect(self, code):
        # close the connection
        print("Socket disconnected with code", code)
        #await self.close()
       
   

    def receive(self, data):
        print("receive")
        sleep(1)

        #await self.send({"text":str(random.randint(0,100))})
        # the websocket doesn't recieve anything currently from the client
        #pass
    
    async def send_user(self, event):
        self.send(json.dumps({"ping": "pong"}))


