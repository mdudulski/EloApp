# Generated by Django 3.0.4 on 2020-03-17 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200317_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='complete',
        ),
    ]