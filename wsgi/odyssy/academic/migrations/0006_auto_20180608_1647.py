# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-08 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_auto_20180602_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='name',
            field=models.CharField(blank=True, help_text='B.Tech, M.Tech or P.hD.', max_length=50, null=True),
        ),
    ]