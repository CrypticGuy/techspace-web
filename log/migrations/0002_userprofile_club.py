# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='club',
            field=models.CharField(choices=[('nothing', 'nothing'), ('codeschool', 'codeschool'), ('cogitans', 'cogitans'), ('ecell', 'ecell'), ('electrotech', 'electrotech'), ('oslc', 'oslc'), ('renderedusict', 'renderedusict'), ('turingai', 'turingai'), ('techspace', 'techspace')], default='nothing', max_length=255),
        ),
    ]
