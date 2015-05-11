# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=60, blank=True)),
                ('value', models.CharField(max_length=2000, blank=True)),
                ('slaveOnly', models.NullBooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('link', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='citations',
            field=models.ManyToManyField(to='Builder.Citation', blank=True),
        ),
        migrations.AddField(
            model_name='case',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='Builder.Case', null=True),
        ),
    ]
