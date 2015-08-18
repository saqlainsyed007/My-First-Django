# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20150806_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='new_field',
            field=models.ImageField(default=False, upload_to=b''),
        ),
    ]
