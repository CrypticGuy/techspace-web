# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-10 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_merge_20170910_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='club',
            field=models.CharField(blank=True, choices=[('codeschool', 'Codeschool'), ('cogitans', 'Cogitans'), ('droidclub', 'Droid Club'), ('ecell', 'E-Cell'), ('electrotech', 'Electrotech'), ('oslc', 'OSLC'), ('renderedusict', 'Rendered-USICT'), ('turingai', 'Turing A.I.')], max_length=200),
        ),
    ]
