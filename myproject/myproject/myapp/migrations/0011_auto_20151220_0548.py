# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_executedcoument'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExecuteDcoument',
            new_name='ExecuteDocument',
        ),
    ]
