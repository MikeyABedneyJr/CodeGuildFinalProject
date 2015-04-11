# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0003_remove_userprofile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.OneToOneField(null=True, blank=True, to='pdxart.Address'),
            preserve_default=True,
        ),
    ]
