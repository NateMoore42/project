import re, random

from django import forms
from django.forms import ModelForm
from character.models import *
from django.utils.translation import ugettext_lazy as _
from character.variables.vars import *

class CreationForm(forms.ModelForm):
    error_css_class = 'error'

    c_name = forms.CharField(strip=False)
    description = forms.CharField(max_length=1000, required=False)
    background = forms.ChoiceField(choices=ALL_BACKGROUNDS, required=True)

    age = forms.IntegerField(initial=21)
    experience = forms.IntegerField(initial=0)
    height = forms.IntegerField(initial=192)
    weight = forms.IntegerField(initial=207)

    language = forms.ModelMultipleChoiceField(queryset=Language.objects.all())
    skills = forms.ModelMultipleChoiceField(queryset=Skills.objects.all())
    feats = forms.ModelMultipleChoiceField(queryset=Feats.objects.all())
    c_class = forms.ModelMultipleChoiceField(queryset=CharClass.objects.all())

    race = forms.ChoiceField(choices=ALL_RACES, required=True)
    subrace = forms.ChoiceField(choices=ALL_SUBRACES, required=True)
    gender = forms.ChoiceField(choices=GENDERS)
    alignment = forms.ChoiceField(choices=ALIGNMENTS, required=True)
    can_fly = forms.BooleanField(required=False)
    movement = forms.IntegerField(initial=25)

    dexterity = forms.IntegerField(required=True)
    strength = forms.IntegerField(required=True)
    constitution = forms.IntegerField(required=True)
    charisma = forms.IntegerField(required=True)
    wisdom = forms.IntegerField(required=True)
    intelligence = forms.IntegerField(required=True)

    class Meta:
        model = Character

        fields = ('c_name', 'level', 'hp', 'background',
                  'age', 'weight', 'height', 'experience', 'language',
                  'c_class', 'race', 'subrace', 'gender', 'description',
                  'alignment', 'dexterity', 'strength', 'constitution',
                  'charisma', 'wisdom', 'intelligence', 'skills',
                  'ideals', 'bonds', 'p_traits', 'flaws', 'feats',
                  'movement', 'can_fly', 'character_portrait')

        exclude = ('player',)

    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
