# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151025_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='bus_c',
            new_name='business',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='type_c',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='bus_e',
            new_name='business',
        ),
        migrations.RemoveField(
            model_name='event',
            name='type_e',
        ),
        migrations.AddField(
            model_name='event',
            name='kind',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Facebook'), (1, b'Twitter'), (2, b'Instagram'), (3, b'Email'), (4, b'Soir\xc3\xa9e'), (5, b'T\xc3\xa9l\xc3\xa9phone'), (6, b'RDV')]),
        ),
    ]
