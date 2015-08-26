# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2015, 8, 26, 5, 47, 36, 131239, tzinfo=utc))),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comment',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'word', 'verbose_name_plural': 'word'},
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
