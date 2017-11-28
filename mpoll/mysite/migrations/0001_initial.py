# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.CharField(default=None, max_length=50)),
                ('enabled', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pollitem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('imagr_url', models.URLField(default=b'https://imgur.com/gallery/Ni56S.png')),
                ('vote', models.PositiveIntegerField(default=0)),
                ('poll', models.ForeignKey(to='mysite.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='VoteCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.PositiveIntegerField()),
                ('pollid', models.PositiveIntegerField()),
                ('pollitemid', models.PositiveIntegerField()),
                ('vote_date', models.DateField()),
            ],
        ),
    ]
