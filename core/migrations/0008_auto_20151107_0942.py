# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151107_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='left',
            field=models.ForeignKey(related_name='left_level', blank=True, to='core.Partner', null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='right',
            field=models.ForeignKey(related_name='right_level', blank=True, to='core.Partner', null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='up',
            field=models.ForeignKey(related_name='up_level', blank=True, to='core.Partner', null=True),
        ),
    ]
