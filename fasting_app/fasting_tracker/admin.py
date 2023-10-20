# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FastingSession
from ..core.mixins import AuditableAdminMixin


@admin.register(FastingSession)
class FastingSessionAdmin(AuditableAdminMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'start_date',
        'end_date',
        'duration',
        'target_duration',
        'comments',
    )
    list_filter = ('created', 'modified', 'user', 'start_date', 'end_date')
