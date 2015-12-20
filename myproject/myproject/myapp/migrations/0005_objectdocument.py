# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_sourcedocument_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objname', models.CharField(max_length=256, null=True)),
                ('stdout', models.CharField(max_length=2048, null=True)),
                ('stderr', models.CharField(max_length=2048, null=True)),
                ('p_status', models.CharField(max_length=2048, null=True)),
            ],
        ),
    ]
