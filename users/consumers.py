import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UserActivityConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            self.user = self.scope['user']
            await self.channel_layer.group_add('online_users', self.channel_name)
            await self.accept()
            await self.update_user_activity()

    async def disconnect(self, close_code):
        if self.scope['user'].is_authenticated:
            await self.channel_layer.group_discard('online_users', self.channel_name)

    async def update_user_activity(self):
        await self.channel_layer.group_send(
            'online_users',
            {
                'type': 'user_activity',
                'user_id': self.user.id,
            }
        )

    async def user_activity(self, event):
        pass
