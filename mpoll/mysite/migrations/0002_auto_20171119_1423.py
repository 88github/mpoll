# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollitem',
            old_name='imagr_url',
            new_name='image_url',
        ),
        migrations.AlterField(
            model_name='poll',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
