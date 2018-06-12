# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-12 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_people_link_gh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='academic_highlights',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='academic_qualifications',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='administrative_experience',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='area_of_interest',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='institute',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='office',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='other',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='post',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='professional_memberships',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='publications',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='teaching',
            field=models.TextField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='work_experience',
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
    ]
