# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0006_auto_20170314_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='I3IO3vUHyhPPL2VoBnnDWrk2', max_length=24),
        ),
    ]
