# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0011_auto_20150420_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='medium',
            field=models.ForeignKey(to='pdxart.Medium', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
