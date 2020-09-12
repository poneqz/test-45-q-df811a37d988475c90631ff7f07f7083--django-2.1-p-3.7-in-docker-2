# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .choices import LocationTypeChoices, StatusTypeChoices


class Leads(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    mobile = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    location_type = models.CharField(max_length=10, choices=LocationTypeChoices.choices,
                                     default=LocationTypeChoices.CITY)
    location = models.TextField(null=False, default="")
    status = models.CharField(max_length=10, choices=StatusTypeChoices.choices, default=StatusTypeChoices.Created)
    communication = models.TextField(default="", blank=True, null=True)

    # REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile', 'email', 'location_type', 'location']

    def __self__(self):
        return self.first_name + "" + self.last_name
