# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20151217_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcedocument',
            name='docfile',
            field=models.FileField(upload_to=b'documents/source'),
        ),
    ]
