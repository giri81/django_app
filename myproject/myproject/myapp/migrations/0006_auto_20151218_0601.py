# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_objectdocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectdocument',
            name='id',
        ),
        migrations.AlterField(
            model_name='objectdocument',
            name='objname',
            field=models.CharField(default=True, max_length=256, serialize=False, primary_key=True),
        ),
    ]
