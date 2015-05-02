# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0012_auto_20150428_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'/media/profile_images', blank=True),
            preserve_default=True,
        ),
    ]
