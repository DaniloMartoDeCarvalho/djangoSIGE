from __future__ import unicode_literals

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'djangosige.apps.base'
    default_auto_field = 'django.db.models.BigAutoField'
