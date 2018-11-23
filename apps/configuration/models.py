# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class Schema(models.Model):
    data = JSONField()

    def __unicode__(self):
        base_name = '[{}]-[{}]-'.format(self.data['title'], self.data['type'])
        if self.data['type'] == 'object':
            base_name += '-'.join(self.data['properties'].keys())
        elif self.data['type'] == 'array':
            base_name += '-'.join(self.data['items']['properties'].keys())
        return base_name


class Configuration(models.Model):
    schema = models.ForeignKey(Schema)
    data = JSONField(null=True, blank=True)
