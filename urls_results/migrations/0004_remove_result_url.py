# Generated by Django 3.1.3 on 2021-02-01 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urls_results', '0003_result_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='url',
        ),
    ]
