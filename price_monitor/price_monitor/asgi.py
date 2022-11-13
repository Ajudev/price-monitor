"""
ASGI config for price_monitor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_monitor.settings')

# application = get_asgi_application()

# from sockets.auth import TokenAuthMiddleware
# from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from sockets.routing import websocket_urlpatterns
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_monitor.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":URLRouter(websocket_urlpatterns),
})
