# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique Identifier.', unique=True, verbose_name='Unique Identifier')),
                ('is_active', models.BooleanField(default=True, help_text='Active or not.', verbose_name='Active')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Creation date.', verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, help_text='Last update date.', verbose_name='Date Updated')),
                ('email', models.EmailField(help_text='Email address of the user.', max_length=254, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(blank=True, help_text='First name of the user.', max_length=64, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, help_text='Last name of the user.', max_length=64, verbose_name='Last Name')),
                ('is_staff', models.BooleanField(default=False, help_text='Identify whether the user is a staff or not.', verbose_name='Staff Status')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'user_users',
                'verbose_name': 'User',
            },
        ),
    ]
