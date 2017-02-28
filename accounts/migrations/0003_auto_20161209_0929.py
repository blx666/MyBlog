# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 09:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Category')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='accepted_eula',
            field=models.NullBooleanField(),
        ),
    ]