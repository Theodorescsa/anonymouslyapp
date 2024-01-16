import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract the room name from the URL route parameters
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Add the user to the room's group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the user from the room's group when the WebSocket closes
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        # Receive a message from the WebSocket

        # Parse the JSON message
        message_data = json.loads(text_data)
        message = message_data['message']

        # Send the message to the room's group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        # Receive the message from the room's group and send it to the WebSocket

        message = event['message']

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))
