# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0020_auto_20170324_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='nGPkhtCHK9bFyw1weHo9Jv9s', max_length=24),
        ),
    ]
