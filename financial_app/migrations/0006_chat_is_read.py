# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_app', '0005_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
