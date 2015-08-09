# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image_name',
            field=models.CharField(default=b'img', max_length=30),
        ),
        migrations.AddField(
            model_name='extras',
            name='image_name',
            field=models.CharField(default=b'img', max_length=30),
        ),
    ]
