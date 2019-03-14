# coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Schema, Configuration


class SchemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schema
        fields = ('url', 'data')


class ConfigurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuration
        fields = ('name', 'schema', 'data')
