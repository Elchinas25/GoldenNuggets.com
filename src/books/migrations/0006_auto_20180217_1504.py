# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_average'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-average']},
        ),
        migrations.AlterModelOptions(
            name='nugget',
            options={'ordering': ['-average']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
