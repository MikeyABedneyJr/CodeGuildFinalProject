# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0006_auto_20150413_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='LinkedIn',
            new_name='linkedin',
        ),
    ]
