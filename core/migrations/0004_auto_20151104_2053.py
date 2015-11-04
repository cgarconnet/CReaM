# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151025_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='kind',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Customer'), (1, 'Dealer'), (2, 'Host')]),
        ),
        migrations.AlterField(
            model_name='event',
            name='kind',
            field=models.IntegerField(blank=True, null=True, choices=[(0, 'Facebook'), (1, 'Twitter'), (2, 'Instagram'), (3, 'Email'), (4, 'Soir\xe9e'), (5, 'T\xe9l\xe9phone'), (6, 'RDV')]),
        ),
    ]
