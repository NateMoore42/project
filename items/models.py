from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.http import urlquote
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from character.variables.vars import *

class Armor(models.Model):
    armor = models.CharField(max_length=50, choices=ALL_ARMOR)
    armor_type = models.CharField(max_length=50, choices=ALL_ARMOR_TYPES)
    cost = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=500)

    def __unicode__(self):
        return str(self.armor)

class Tools(models.Model):
    tool = models.CharField(max_length=50, choices=ARTISANS_TOOLS)
    cost = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'tool'
        verbose_name_plural = 'tools'

    def __unicode__(self):
        return str(self.tool)

class Kits(models.Model):
    kit = models.CharField(max_length=50, choices=ALL_KITS)
    cost = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'kit'
        verbose_name_plural = 'kits'

    def __unicode__(self):
        return str(self.kit)

class Sets(models.Model):
    i_set = models.CharField(max_length=50, choices=ALL_SETS)
    cost = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'set'
        verbose_name_plural = 'sets'

    def __unicode__(self):
        return str(self.i_set)

class Instruments(models.Model):
    instrument = models.CharField(max_length=50, choices=ALL_INSTRUMENTS)
    cost = models.IntegerField()
    weight = models.FloatField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'instrument'
        verbose_name_plural = 'instruments'

    def __unicode__(self):
        return str(self.instrument)

class MountItems(models.Model):
    m_item = models.CharField(max_length=50, choices=MOUNT_ITEMS)
    cost = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'mount item'
        verbose_name_plural = 'mount items'

    def __unicode__(self):
        return str(self.m_item)

class Vehicles(models.Model):
    vehicle = models.CharField(max_length=50, choices=VEHICLES)
    cost = models.IntegerField()
    weight = models.IntegerField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'vehicle'
        verbose_name_plural = 'vehicles'

    def __unicode__(self):
        return str(self.vehicle)

class Mounts(models.Model):
    mount = models.CharField(max_length=50, choices=ALL_MOUNTS, default='None')
    mount_type = models.CharField(max_length=10, choices=MOUNT_TYPE)
    cost = models.IntegerField()
    speed = models.FloatField()
    capacity = models.IntegerField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'mount'
        verbose_name_plural = 'mounts'

    def __unicode__(self):
        return str(self.mount)
