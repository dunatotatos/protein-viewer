# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-14 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionId', models.CharField(default=b'', max_length=100)),
                ('tempDir', models.CharField(default=b'', max_length=100)),
            ],
        ),
    ]
