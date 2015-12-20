# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20151218_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecuteDcoument',
            fields=[
                ('executablename', models.CharField(default=True, max_length=256, serialize=False, primary_key=True)),
                ('stdout', models.CharField(max_length=2048, null=True)),
                ('stderr', models.CharField(max_length=2048, null=True)),
                ('p_status', models.CharField(max_length=2048, null=True)),
            ],
        ),
    ]
