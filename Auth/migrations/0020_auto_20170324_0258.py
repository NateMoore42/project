# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0019_auto_20170324_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='9EQ5MPF7zv0ZoeJRJFBKOGEJ', max_length=24),
        ),
    ]