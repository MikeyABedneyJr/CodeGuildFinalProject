# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0003_auto_20150408_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='apartment_or_pobox',
        ),
        migrations.RemoveField(
            model_name='address',
            name='compass',
        ),
        migrations.RemoveField(
            model_name='address',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street_name',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='street_address',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
