# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdxart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=b'Oregon', max_length=128)),
                ('house_number', models.IntegerField(default=0, max_length=128)),
                ('street_name', models.CharField(default=0, max_length=128)),
                ('apartment_or_pobox', models.CharField(default=0, max_length=128)),
                ('compass', models.CharField(default=0, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(default=0, to='pdxart.Address'),
            preserve_default=True,
        ),
    ]
