# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-08 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ONGOING', 'Ongoing'), ('PLACED', 'Placed'), ('CONFIRMED', 'Confirmed'), ('OUTFORDELIVERY', 'Out For Delivery'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='PLACED', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.FloatField(),
        ),
    ]