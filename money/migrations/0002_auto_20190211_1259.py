# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-11 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='recieving_party',
            new_name='receiving_party',
        ),
    ]
