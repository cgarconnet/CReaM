# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_c', models.IntegerField(blank=True, null=True, choices=[(0, b'Customer'), (1, b'Partner'), (2, b'Host')])),
                ('status', models.IntegerField(blank=True, null=True, choices=[(0, b'Prospect - New'), (1, b'Prospect - Cold'), (2, b'Prospect - Hot'), (3, b'Active'), (4, b'Active - cold'), (5, b'Active - Hot')])),
                ('fullname', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bus_c', models.ForeignKey(to='core.Business')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_e', models.IntegerField(blank=True, null=True, choices=[(0, b'Facebook'), (1, b'Twitter'), (2, b'Instagram'), (3, b'Email'), (4, b'Soir\xc3\xa9e'), (5, b'T\xc3\xa9l\xc3\xa9phone'), (6, b'Soir\xc3\xa9e'), (7, b'RDV')])),
                ('description', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bus_e', models.ForeignKey(to='core.Business')),
                ('customer', models.ForeignKey(to='core.Customer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
