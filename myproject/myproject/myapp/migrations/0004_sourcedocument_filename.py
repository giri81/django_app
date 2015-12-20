# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20151217_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcedocument',
            name='filename',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
