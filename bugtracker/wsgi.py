"""
WSGI config for bugtracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bugtracker.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')
# from django.core.wsgi import get_wsgi_application
from configurations.wsgi import get_wsgi_application


application = get_wsgi_application()
