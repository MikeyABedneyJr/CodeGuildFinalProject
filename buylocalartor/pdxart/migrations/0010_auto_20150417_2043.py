# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0009_auto_20150416_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profilepic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'/media/profile_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.OneToOneField(null=True, blank=True, to='pdxart.Profilepic'),
            preserve_default=True,
        ),
    ]
