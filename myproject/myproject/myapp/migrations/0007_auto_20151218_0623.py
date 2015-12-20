# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import myproject.myapp.storage


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20151218_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcedocument',
            name='filename',
        ),
        migrations.AlterField(
            model_name='sourcedocument',
            name='docfile',
            field=models.FileField(storage=myproject.myapp.storage.OverwriteStorage(), upload_to=b'documents/source'),
        ),
    ]
