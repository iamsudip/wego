# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-27 18:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='Unique Identifier')),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='Unique Identifier')),
                ('allowed_condiments', models.ManyToManyField(blank=True, to='menu.Condiment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='Unique Identifier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='Unique Identifier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizedItemPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Item')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('trashed', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.CharField(max_length=256, unique=True, verbose_name='Unique Identifier')),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ItemGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='allowed_variants',
            field=models.ManyToManyField(blank=True, to='menu.Variant'),
        ),
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ItemGroup'),
        ),
        migrations.AddField(
            model_name='condiment',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.ItemGroup'),
        ),
    ]
