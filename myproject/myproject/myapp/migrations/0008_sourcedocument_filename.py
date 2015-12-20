# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20151218_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcedocument',
            name='filename',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
