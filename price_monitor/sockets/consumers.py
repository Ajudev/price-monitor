import json
from channels.generic.websocket import AsyncWebsocketConsumer


class RatesConsumer(AsyncWebsocketConsumer):
    """
    Class which defines the logic for websocket connection. It defines method on what happens when users
    connect to websocket, disconnect etc.
    """
    async def connect(self):
        self.room_group_name = 'broadcast'

        # Add user to group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.send(text_data=json.dumps({"message":"Registered to receive live rates data"}))

    async def disconnect(self, close_code):
        # Remove user from group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        if text_data.lower() == "exit":
            await self.send(text_data=json.dumps({"message":"Disconnected from service"}))
            await self.close()

    async def send_message(self, event):
        # Send message to group
        data = event['data']
        await self.send(text_data=json.dumps({
            'message': data
        }))
