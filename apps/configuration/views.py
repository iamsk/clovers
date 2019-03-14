# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .models import Schema, Configuration
from .serializers import SchemaSerializer, ConfigurationSerializer


class SchemaView(viewsets.ReadOnlyModelViewSet):
    serializer_class = SchemaSerializer
    queryset = Schema.objects.all()


class ConfigurationView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()
    lookup_field = 'name'
