# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0021_auto_20170324_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='eMiUIo9JVq0J5zO3FNreqoEz', max_length=24),
        ),
    ]
