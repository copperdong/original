# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-28 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180707_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cms_user',
            field=models.BooleanField(default=False),
        ),
    ]
