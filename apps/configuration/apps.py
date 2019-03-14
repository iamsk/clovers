# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ConfigurationConfig(AppConfig):
    name = 'apps.configuration'

    def ready(self):
        import signals  # noqa
