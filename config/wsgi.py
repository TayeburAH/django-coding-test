"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from py_dotenv import read_dotenv

from django.core.wsgi import get_wsgi_application

read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.example'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
