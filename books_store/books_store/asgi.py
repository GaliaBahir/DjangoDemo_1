"""
ASGI config for books_store project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_store.settings')

from books_store.ws_urlpatterns import ws_urlpatterns

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(ws_urlpatterns)
})
