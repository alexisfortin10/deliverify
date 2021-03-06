# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthAppShopUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('myshopify_domain', models.CharField(editable=False, max_length=255, unique=True)),
                ('token', models.CharField(default=b'00000000000000000000000000000000', editable=False, max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuthShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(editable=False, max_length=255, unique=True)),
                ('shop_id', models.CharField(editable=False, max_length=255, unique=True)),
                ('token', models.CharField(default=b'00000000000000000000000000000000', editable=False, max_length=32)),
            ],
        ),
    ]
