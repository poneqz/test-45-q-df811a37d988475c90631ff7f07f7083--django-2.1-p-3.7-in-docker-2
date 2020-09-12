# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Leads


class LeadsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'mobile',
                    'email',
                    'location_type',
                    'location',
                    'status',
                    'communication',)
    list_filter = ('status',)


admin.site.register(Leads, LeadsAdmin)
