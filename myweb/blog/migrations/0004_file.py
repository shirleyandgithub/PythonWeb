# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_publisher_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('fileway', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]