"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

import sys

from django.core.asgi import get_asgi_application

from fastapi import FastAPI

from fastapi.middleware.wsgi import WSGIMiddleware

# Импортируем ваше FastAPI приложение
from api.fastapi_app import app as fastapi_app

# Добавляем корневую папку проекта в PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()

django_asgi_app = WSGIMiddleware(application)

app = FastAPI()

# Монтируем Django приложение в FastAPI
app.mount("/django", WSGIMiddleware(application))
