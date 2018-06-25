# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique Identifier.', unique=True, verbose_name='Unique Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Active or not.', verbose_name='Active')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Creation date.', verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, help_text='Last update date.', verbose_name='Date Updated')),
                ('task_name', models.CharField(help_text='Detailed task name.', max_length=128, verbose_name='Task Name')),
                ('is_completed', models.BooleanField(default=False, help_text='Completed or not.', verbose_name='Completed')),
            ],
            options={
                'verbose_name_plural': 'To Dos',
                'db_table': 'tasks_to_dos',
                'verbose_name': 'To Do',
            },
        ),
    ]
