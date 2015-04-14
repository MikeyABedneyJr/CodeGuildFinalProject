# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0005_auto_20150410_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medium',
            options={'verbose_name_plural': 'Media'},
        ),
    ]
