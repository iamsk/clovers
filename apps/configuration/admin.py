# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django_admin_json_editor import JSONEditorWidget
from django_json_schema_editor.widgets import JSONSchemaEditorWidget

from .models import Schema, Configuration


def get_schema(id):
    return Schema.objects.get(id=id).data


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'schema', 'data')
    search_fields = ('data',)
    list_filter = ('schema',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['schema', ]
        else:
            return []

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            schema_id = obj.schema.id
            schema = get_schema(schema_id)
        else:
            schema = {}
        widget = JSONEditorWidget(schema, False, True)
        form = super(ConfigurationAdmin, self).get_form(request, obj, widgets={'data': widget}, **kwargs)
        return form


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    search_fields = ('data',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SchemaAdmin, self).get_form(request, obj, widgets={'data': JSONSchemaEditorWidget}, **kwargs)
        return form


admin.site.site_header = 'CLOVERS'
admin.site.index_title = 'Administration'
admin.site.site_title = 'CLOVERS'
