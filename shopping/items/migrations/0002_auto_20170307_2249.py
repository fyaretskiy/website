# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpurchaseditem',
            name='list_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_purchased_items', to='items.Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpurchaseditem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_purchased_items', to='user.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usershoppinglistitem',
            name='list_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_shopping_list_items', to='items.Item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usershoppinglistitem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user_shopping_list_items', to='user.User'),
            preserve_default=False,
        ),
    ]