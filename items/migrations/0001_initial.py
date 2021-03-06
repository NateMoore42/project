# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armor', models.CharField(choices=[(b'Padded Armour', b'Padded Armour'), (b'Leather Armour', b'Leather Armour'), (b'Studded Leather Armour', b'Studded Leather Armour'), (b'Hide Armour', b'Hide Armour'), (b'Chain Shirt', b'Chain Shirt'), (b'Scale Mail', b'Scale Mail'), (b'Breastplate', b'Breastplate'), (b'Half-Plate Armour', b'Half-Plate'), (b'Ring Mail', b'Ring Mail'), (b'Chain mail', b'Chain Mail'), (b'Splint Armour', b'Splint Armour'), (b'Plate Armour', b'Plate Armour')], max_length=50)),
                ('armor_type', models.CharField(choices=[(b'No Armour', b'Unarmored'), (b'Natural Armour', b'Natural Armor'), (b'Light Armour', b'Light Armor'), (b'Medium Armour', b'Medium Armor'), (b'Heavy Armour', b'Heavy Armor')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.CharField(choices=[(b'Bagpipes', b'Bagpipes'), (b'Drum', b'Drum'), (b'Dulcimer', b'Dulcimer'), (b'Flute', b'Flute'), (b'Lute', b'Lute'), (b'Lyre', b'Lyre'), (b'Horn', b'Horn'), (b'Pan Flute', b'Pan Flute'), (b'Shawm', b'Shawm'), (b'Viol', b'Viol')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'instrument',
                'verbose_name_plural': 'instruments',
            },
        ),
        migrations.CreateModel(
            name='Kits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit', models.CharField(choices=[(b"Herbalist's Kit", b"Herbalist's Kit"), (b"Poisoner's Kit", b"Poisoner's Kit"), (b'Disguise Kit', b'Disguise Kit'), (b'Forgery Kit', b'Forgery Kit')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'kit',
                'verbose_name_plural': 'kits',
            },
        ),
        migrations.CreateModel(
            name='MountItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_item', models.CharField(choices=[(b'Feed', b'Feed'), (b'Griffon Feed', b'Griffon Feed'), (b'Saddle', b'Saddle'), (b'Exotic Saddle', b'Exotic Saddle'), (b'Military Saddle', b'Military Saddle'), (b'Riding Saddle', b'Riding Saddle'), (b'Pack Saddle', b'Pack Saddle'), (b'Saddlebags', b'Saddlebags'), (b'Stabling', b'Stabling')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'mount item',
                'verbose_name_plural': 'mount items',
            },
        ),
        migrations.CreateModel(
            name='Mounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mount', models.CharField(choices=[(b'None', b'None'), (b'Camel', b'Camel'), (b'Donkey', b'Donkey'), (b'Elephant', b'Elephant'), (b'Draft Horse', b'Draft Horse'), (b'Riding Horse', b'Riding Horse'), (b'Mastiff', b'Mastiff'), (b'Pony', b'Pony'), (b'Warhorse', b'Warhorse'), (b'Griffon', b'Griffon'), (b'Galley', b'Galley'), (b'Keelboat', b'Keelboat'), (b'Longship', b'Longship'), (b'Rowboat', b'Rowboat'), (b'Sailing Ship', b'Sailing Ship'), (b'Warship', b'Warship')], default='None', max_length=50)),
                ('mount_type', models.CharField(choices=[(b'Air', b'Air'), (b'Water', b'Water'), (b'Land', b'Land')], max_length=10)),
                ('cost', models.IntegerField()),
                ('speed', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'mount',
                'verbose_name_plural': 'mounts',
            },
        ),
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_set', models.CharField(choices=[(b'Dragonchess Set', b'Dragonchess Set'), (b'Playing Card Set', b'Playing Card Set'), (b'Three-Dragon Ante Set', b'Three-Dragon Ante Set'), (b'Dice Set', b'Dice Set')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'set',
                'verbose_name_plural': 'sets',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool', models.CharField(choices=[(b"Leatherworker's Tools", b"Leatherworker's Tools"), (b"Cartographer's Tools", b"Cartographer's Tools"), (b"Glassblower's Tools", b"Glassblower's Tools"), (b"Woodcarver's Tools", b"Woodcarver's Tools"), (b"Carpenter's Tools", b"Carpenter's Tools"), (b"Navigator's Tools", b"Navigator's Tools"), (b"Cobbler's Tools", b"Cobblser's Tools"), (b"Tinker's Tools", b"Tinker's Tools"), (b"Weaver's Tools", b"Weaver's Tools"), (b"Potter's Tools", b"Potter's Tools"), (b"Jeweller's Tools", b"Jewler's Tools"), (b"Mason's Tools", b"Mason's Tools"), (b"Smith's Tools", b"Smith's Tools"), (b"Thief's Tools", b"Thief's Tools"), (b"Alchemist's Supplies", b"Alchemist's Supplies"), (b"Brewer's Supplies", b"Brewer's Supplies"), (b"Calligrapher's Supplies", b"Calligrapher's Suppplies"), (b"Cook's Utensils", b"Cook's Utensils"), (b"Painter's Suppliers", b"Painter's Supplies")], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.FloatField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'tool',
                'verbose_name_plural': 'tools',
            },
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(choices=[(b'Barding', b'Barding'), (b'Carriage', b'Carriage'), (b'Cart', b'Cart'), (b'Chariot', b'Chariot'), (b'Sled', b'Sled'), (b'Wagon', b'Wagon')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'vehicle',
                'verbose_name_plural': 'vehicles',
            },
        ),
    ]
