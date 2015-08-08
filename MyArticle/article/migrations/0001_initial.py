# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_name', models.CharField(max_length=50)),
                ('article_value', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='extras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rel_article_name', models.CharField(max_length=50)),
            ],
        ),
    ]
