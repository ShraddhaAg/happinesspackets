# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_blacklistedemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklistedemail',
            name='stripped_email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
