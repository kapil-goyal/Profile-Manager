# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-15 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proman', '0011_auto_20171116_0349'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='ContinuingStudents',
            new_name='ContinuingStudent',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
