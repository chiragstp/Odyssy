# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(upload_to='people_images/')),
                ('post', models.CharField(max_length=50)),
                ('academic_highlights', models.CharField(blank=True, max_length=200, null=True)),
                ('committee', models.CharField(blank=True, max_length=50, null=True)),
                ('area_of_interest', models.CharField(blank=True, max_length=500, null=True)),
                ('office', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('faculty', 'Faculty'), ('staff', 'Staff'), ('visiting_faculty', 'Visiting Faculty'), ('administrative', 'Administration')], default='staff', max_length=16)),
                ('academic_qualifications', models.TextField(blank=True, max_length=500, null=True)),
                ('professional_memberships', models.TextField(blank=True, max_length=500, null=True)),
                ('work_experience', models.TextField(blank=True, max_length=500, null=True)),
                ('administrative_experience', models.TextField(blank=True, max_length=200, null=True)),
                ('publications', models.TextField(blank=True, max_length=10000, null=True)),
                ('teaching', models.TextField(blank=True, max_length=200, null=True)),
                ('other', models.TextField(blank=True, max_length=200, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'People',
                'verbose_name_plural': 'People',
            },
        ),
    ]
