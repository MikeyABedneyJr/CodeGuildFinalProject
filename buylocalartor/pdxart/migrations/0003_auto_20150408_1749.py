# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0002_auto_20150408_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(to='pdxart.Address', blank=True),
            preserve_default=True,
        ),
    ]
