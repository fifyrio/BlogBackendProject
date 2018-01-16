# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-16 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QiniuTokenRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(help_text='请求者IP', verbose_name='请求者IP')),
                ('token', models.CharField(help_text='token', max_length=20, verbose_name='token')),
                ('use_type', models.CharField(choices=[('comment', '评论')], help_text='使用类型', max_length=15, verbose_name='使用类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='发送时间', verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '七牛云请求Token',
                'verbose_name_plural': '七牛云请求Token',
            },
        ),
    ]
