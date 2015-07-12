# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
