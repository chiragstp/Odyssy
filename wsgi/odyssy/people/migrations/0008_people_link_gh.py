# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-12 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20180612_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='link_gh',
            field=models.URLField(blank=True, default='#', max_length=400, null=True),
        ),
    ]