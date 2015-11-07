# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100, null=True, blank=True)),
                ('points', models.IntegerField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('left', models.ForeignKey(related_name='left_level', to='core.Partner')),
                ('right', models.ForeignKey(related_name='right_level', to='core.Partner')),
                ('up', models.ForeignKey(related_name='up_level', to='core.Partner')),
            ],
        ),
    ]
