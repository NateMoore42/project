from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

import bulk_admin

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Player'), {'fields': ('player',)}),
        (_('Character Info'), {'fields': ('c_name', 'c_class', 'race', 'subrace', 'age', 'gender', 'height', 'weight')}),
        (_('Stat Info'), {'fields': ('hp', 'dexterity', 'strength', 'intelligence', 'wisdom', 'charisma', 'constitution')}),
        (_('Misc Info'), {'fields': ('language', 'skills', 'alignment', 'feats', 'background', 'description')}),
        (_('Character Portrait'), {'fields': ('character_portrait',)}),
    )

    icon = '<i class="material-icons">group_add</i>'

    list_display = ['c_name', 'player', 'race', 'subrace',]


admin.site.register(Character, CharacterAdmin)

class WeaponAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Weapon'), {'fields': ('weapon',)}),
        (_('Damage Info'), {'fields': ('dice', 'damage', 'damage_type')}),
        (_('Versatile Info'), {'fields': ('versatile_dice', 'versatile_damage')}),
        (_('Weapon Info'), {'fields': ('weapon_class', 'cost', 'weight',)}),
        (_('Properties'), {'fields': ('property1', 'property2', 'property3', 'property4')}),
        (_('Range Info'), {'fields': ('effective_range', 'maximum_range', 'ammo_type')}),
    )

    icon = '<i class="material-icons">add_circle</i>'

    list_display = ['weapon', 'weapon_class', 'property1', 'property2',]

admin.site.register(Weapon, WeaponAdmin)
"""
class InventoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Character'), {'fields': ('character',)}),
        (_('Currency Info'), {'fields': ('copper', 'silver', 'electrum', 'gold', 'platinum')}),
        (_('Equipment Info'), {'fields': ('weapons', 'armor')}),
        (_('Tool Info'), {'fields': ('tools', 'kits', 'sets', 'instruments')}),
        (_('Mount Info'), {'fields': ('m_items', 'vehicles', 'mounts')}),
    )

    icon = '<i class="material-icons">archive</i>'

    list_display = ['character',]

admin.site.register(Inventory, InventoryAdmin)
"""
class FeatAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['feat']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Feats, FeatAdmin)

class LanguageAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['language', 'language_script']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Language, LanguageAdmin)

class SkillsAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['skills', 'check_type']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Skills, SkillsAdmin)

class CharClassAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['c_class']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(CharClass, CharClassAdmin)
