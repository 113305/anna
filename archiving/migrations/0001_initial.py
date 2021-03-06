# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-02 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_year', models.IntegerField()),
                ('materials', models.CharField(max_length=100)),
                ('size_height', models.IntegerField()),
                ('size_width', models.IntegerField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
