# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-15 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0013_auto_20171116_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='iitg.png', upload_to='profile_image'),
        ),
    ]
