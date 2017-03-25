from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *

import bulk_admin

class MountAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Mount Info'), {'fields': ('mount', 'mount_type', 'cost')}),
        (_('Mount Stats'), {'fields': ('speed', 'capacity')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['mount']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Mounts, MountAdmin)

class VehicleAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Vehicle Info'), {'fields': ('vehicle', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['vehicle', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Vehicles, VehicleAdmin)

class MountItemAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Mount Item Info'), {'fields': ('m_item', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['m_item', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(MountItems, MountItemAdmin)

class InstrumentAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Instrument Info'), {'fields': ('instrument', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['instrument', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Instruments, InstrumentAdmin)

class SetAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Set Info'), {'fields': ('i_set', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['i_set', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Sets, SetAdmin)

class KitAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Kit Info'), {'fields': ('kit', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['kit', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Kits, KitAdmin)

class ToolAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Tool Info'), {'fields': ('tool', 'cost', 'weight')}),
        (_('Description'), {'fields': ('description',)})

    )
    list_display = ['tool', 'cost', 'weight']

    icon = '<i class="material-icons">add_circle</i>'

admin.site.register(Tools, ToolAdmin)
