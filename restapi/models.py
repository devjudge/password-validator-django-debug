# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models, migrations

# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class CustomBooleanField(models.BooleanField):

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value)


class Users_Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15, validators=[alphanumeric])
    is_logged_in = models.CustomBooleanField()




