# Generated by Django 3.1.3 on 2021-02-01 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_items', '0002_auto_20210201_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='result',
        ),
    ]