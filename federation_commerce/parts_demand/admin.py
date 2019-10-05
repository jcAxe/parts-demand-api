from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

from .models import PartsDemand
import django.contrib.admin.templatetags.admin_list
from django.utils.safestring import mark_safe
from django.conf import settings
import os


@admin.register(PartsDemand)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'delivery_addr', 'contact_info', 'owner', 'conclusion_status')
    fields = ('conclusion_status', 'owner')


def _my_boolean_icon(field_val):
    icon_url = static('imgs/%s.svg' % {True: 'yes', False: 'no', None: 'unknown'}[field_val])
    return format_html('<img src="{}" alt="{}">', icon_url, field_val)


django.contrib.admin.templatetags.admin_list._boolean_icon = _my_boolean_icon
