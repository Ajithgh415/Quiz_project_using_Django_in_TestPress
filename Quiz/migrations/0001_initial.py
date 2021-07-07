# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-23 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('choice_one', models.CharField(max_length=200)),
                ('choice_two', models.CharField(max_length=200)),
                ('choice_three', models.CharField(max_length=200)),
                ('choice_four', models.CharField(max_length=200)),
                ('choice_five', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
            ],
        ),
    ]
