# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0013_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar',
        ),
    ]
