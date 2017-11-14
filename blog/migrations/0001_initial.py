# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('small_description', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]