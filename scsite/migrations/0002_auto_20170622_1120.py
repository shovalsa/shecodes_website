# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 08:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='surename',
            new_name='surname',
        ),
    ]
