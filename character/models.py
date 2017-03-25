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

from datetime import date
import time, os, logging, sys, random, copy, math, uuid
import psycopg2

from Auth.models import User
from variables.vars import *
from items.models import *

class CharacterManager(models.Model):
    def _create_character(self, player,
                          c_name, level, hp, experience,
                          c_class, race, subrace, background,
                          age, weight, height, language,
                          gender, alignment, description,
                          dexterity, strength, constitution,
                          charisma, wisdom, intelligence,
                          skills, character_portrait,
                          slug_id
        ):

        now = timezone.now()
        character = self.model( c_name=c_name, level=level, hp=hp,
                                experience=experience, player=player,
                                c_class=c_class, race=race, subrace=subrace,
                                background=background,
                                age=age, weight=weight, height=height,

                                language=language,

                                gender=gender, alignment=alignment,
                                description=description,

                                dexterity=dexterity, charisma=charisma,
                                intelligence=intelligence, wisdom=wisdom,
                                constitution=constitution, strength=strength,

                                ideals=ideals, p_traits=p_traits, flaws=flaws,
                                bonds=bonds, movement=movement, can_fly=can_fly,
                                feats=feats,

                                skills=skills,
                                character_portrait=character_portrait,
                                slug_id=slug_id,
                                date_created=now, last_edited=now)
        character.save(using=self._db)
        return character

    def create_character(self, player,
                         c_name, level, hp, experience,
                         c_class, race, subrace, background,
                         age, height, weight, language,
                         gender, alignment, description,
                         dexterity, strength, constitution,
                         charisma, wisdom, intelligence,
                         skills, character_portrait,
                         ideals, p_traits, flaws, bonds,
                         movement, can_fly, feats,
                         slug_id):

        return self._create_character(player, level, c_name, hp,
                                      c_class, race, subrace,
                                      age, height, weight, language,
                                      background, experience,
                                      gender, alignment, description,
                                      dexterity, strength, constitution,
                                      charisma, wisdom, intelligence,
                                      skills, character_portrait,

                                      ideals, p_traits, flaws, bonds,
                                      movement, can_fly, feats,
                                      slug_id)

class Character(models.Model):
    player = models.ForeignKey(User, blank=False, related_name="characters")
    c_name = models.CharField(_('character name'), max_length=50)
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=10)
    experience = models.IntegerField(default=0)

    age = models.IntegerField(default=21, null=True, blank=True)
    height = models.IntegerField(default=192, null=True, blank=True)
    weight = models.IntegerField(default=200, null=True, blank=True)

    language = models.ManyToManyField('Language', blank=True)
    skills = models.ManyToManyField('Skills', blank=True)
    c_class = models.ManyToManyField('CharClass', blank=False, verbose_name="class")
    feats = models.ManyToManyField('Feats', blank=True, verbose_name="feats")

    race = models.CharField(max_length=25, choices=ALL_RACES)
    description = models.TextField(max_length=1000, blank=True, null=True)
    ideals = models.CharField(max_length=200, blank=True)
    p_traits = models.CharField(max_length=200, blank=True)
    flaws = models.CharField(max_length=200, blank=True)
    bonds = models.CharField(max_length=200, blank=True)

    subrace = models.CharField(max_length=25, choices=ALL_SUBRACES)
    gender = models.CharField(max_length=15, choices=GENDERS, default='male')
    alignment = models.CharField(max_length=50, choices=ALIGNMENTS)
    background = models.CharField(max_length=50, choices=ALL_BACKGROUNDS)

    movement = models.IntegerField(default=30)
    can_fly = models.BooleanField(default=False)

    dexterity = models.IntegerField()
    charisma = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    constitution = models.IntegerField()
    strength = models.IntegerField()
    character_portrait = models.ImageField(
            upload_to='character-portraits/%Y/%m/%d', blank=True, null=True)

    slug_id = models.CharField(default=get_random_string(length=12), primary_key=True, max_length=12)

    objects = CharacterManager()

    class Meta:
        verbose_name = _('character')
        verbose_name_plural = _('characters')

    def __unicode__(self):
        return u'%s' % self.c_name

    def get_absolute_url(self):
        return "/characters/character/%s/%s" % (self.slug_id, self.c_name)
    def get_by_natural_key(self, c_name):
        return self.get(c_name__iexact=c_name)
    def get_proficiency(self, *args, **kwargs):
        logging.debug('Generating character proficiency...')
        self.proficiency = self.level * 0.25 + 2
        logging.debug('Character proficiency generated.')
        logging.debug('Character proficiency is ' + str(math.floor(self.proficiency)) + '.\n')
        return math.floor(self.proficiency)

class Inventory(models.Model):
    character = models.OneToOneField('Character', on_delete=models.CASCADE)
    weapons = models.ManyToManyField('Weapon', blank=True)
    mounts = models.ManyToManyField(Mounts, blank=True)
    armor = models.ManyToManyField(Armor, blank=True)
    tools = models.ManyToManyField(Tools, blank=True)
    kits = models.ManyToManyField(Kits, blank=True)
    sets = models.ManyToManyField(Sets, blank=True)
    instruments = models.ManyToManyField(Instruments, blank=True)
    m_items = models.ManyToManyField(MountItems, blank=True, verbose_name='Mount Items')
    vehicles = models.ManyToManyField(Vehicles, blank=True)
    copper = models.IntegerField(default=0, blank=True)
    silver = models.IntegerField(default=0, blank=True)
    electrum = models.IntegerField(default=0, blank=True)
    gold = models.IntegerField(default=0, blank=True)
    platinum = models.IntegerField(default=0, blank=True)

    class Meta:
        verbose_name = _('inventory')
        verbose_name_plural = _('inventories')

    def __unicode__(self):
        return u"%s's Inventory" % self.character

    def get_by_natural_key(self, character):
        return self.get(character__iexact=character)

class Feats(models.Model):
    feat = models.CharField(max_length=50, choices=ALL_FEATS, primary_key=True)
    effect = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = _('feat')
        verbose_name_plural = _('feats')

    def __unicode__(self):
        return str(self.feat)

class CharClass(models.Model):
    c_class = models.CharField(max_length=25, primary_key=True, choices=ALL_CLASSES)

    class Meta:
        verbose_name = _('class')
        verbose_name_plural = _('classes')

    def __unicode__(self):
        return str(self.c_class)

class Skills(models.Model):
    skills = models.CharField(max_length=50, primary_key=True, choices=ALL_SKILLS)
    check_type = models.CharField(max_length=50, choices=ALL_CHECK_TYPES)

    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')

    def __unicode__(self):
        return str(self.skills)

class Language(models.Model):
    language = models.CharField(max_length=50, primary_key=True, choices=ALL_LANGUAGES)
    language_script = models.CharField(max_length=50, choices=ALL_LANGUAGE_SCRIPTS)

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __unicode__(self):
        return str(self.language)

class Weapon(models.Model):
    weapon = models.CharField(max_length=50, primary_key=True, choices=ALL_WEAPONS)
    dice = models.IntegerField()
    damage = models.CharField(max_length=4, choices=ALL_DICE)
    versatile_dice = models.IntegerField()
    versatile_damage = models.CharField(max_length=4, choices=ALL_DICE)
    weapon_class = models.CharField(max_length=50, choices=WEAPON_CLASSES)
    damage_type = models.CharField(max_length=50, choices=DAMAGE_TYPES)
    cost = models.IntegerField()
    weight = models.IntegerField()
    property1 = models.CharField(max_length=50, choices=WEAPON_TYPES)
    property2 = models.CharField(max_length=50, choices=WEAPON_TYPES)
    property3 = models.CharField(max_length=50, choices=WEAPON_TYPES)
    property4 = models.CharField(max_length=50, choices=WEAPON_TYPES)
    ammo_type = models.CharField(max_length=50, choices=ALL_AMMUNITION)
    effective_range = models.IntegerField()
    maximum_range = models.IntegerField()

    class Meta:
        verbose_name = 'weapon'
        verbose_name_plural = 'weapons'

    def __unicode__(self):
        return str(self.weapon)

    def _check_proficiency(self, *args, **kwargs):
        pass

class Dice(object):
    def __init__(self, dice, dice_amount, *args, **kwargs):
        self.dice = dice
        self.dice_amount = dice_amount

    def getDiceSides(self, *args, **kwargs):
        self.dice_sides = ALL_DICE[self.dice].get(DICE_SIDES)
        return self.dice_sides
    def rollDice(self, *args, **kwargs):
        #logging.debug('Detected ' + str(self.dice_amount) + ' ' + self.dice + '.')
        #logging.debug('Rolling dice...')
        self.dice_value = random.randint(
            self.dice_sides / self.dice_sides, self.dice_sides
            )
        return self.dice_value
    def rollMultipleDice(self, *args, **kwargs):
        count = 0
        for dice in range(self.dice_amount):
            if self.rollDice() >= 1:
                count += 1
                logging.debug('Rolled ' + str(self.dice_value) + '.\n')
                #logging.debug('Roll ' + str(count) + '.')

        return self.dice_value

@receiver(post_save, sender=Character)
def create_character_inventory(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.create(character=instance)

@receiver(post_save, sender=Character)
def save_character_inventory(sender, instance, **kwargs):
    instance.inventory.save()
