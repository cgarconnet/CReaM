# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151104_2053'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partner',
        ),
    ]
