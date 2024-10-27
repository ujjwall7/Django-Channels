import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from master.consumer import *


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channels.settings')

ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi())
    path('ws/new/', TestConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : URLRouter(ws_patterns)
})
