from django.contrib import admin
from .models import PartsDemand
from django.utils.safestring import mark_safe
from django.conf import settings
import os


@admin.register(PartsDemand)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'delivery_addr', 'contact_info', 'owner', 'conclusion_status')
    fields = ('conclusion_status', 'owner')

