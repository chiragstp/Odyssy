# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_admission_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='programme',
            field=models.CharField(blank=True, choices=[(b'btech', b'mtech'), (b'mtech', b'mtech')], default=b'btech', max_length=16, null=True),
        ),
    ]