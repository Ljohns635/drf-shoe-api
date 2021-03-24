"""
ASGI config for shoestoreserver project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoestoreserver.settings')

application = get_asgi_application()

# While growing up on the African Savannah Joe learned how to farm barley, wheat, peanuts and sugarcane, and became fluent in Maasai/ Maa