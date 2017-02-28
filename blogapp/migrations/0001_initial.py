# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('blogid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='UserBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.UserBlog'),
        ),
    ]