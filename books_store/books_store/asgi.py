"""
ASGI config for books_store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import books_store.urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_store.settings')

application = get_asgi_application()

        
application = ProtocolTypeRouter(
    {
        # handle http/https requests
        "http": get_asgi_application(),
        # handle ws/wss requests
        "websocket": URLRouter(books_store.urls.uwebsocket_urlpatterns)
    }
)