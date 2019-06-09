# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplied', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suppliedlend',
            name='name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='supplied.SuppliedInfo', verbose_name='借用物资名称'),
        ),
    ]
