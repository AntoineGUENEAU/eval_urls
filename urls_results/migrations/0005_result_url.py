# Generated by Django 3.1.3 on 2021-02-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urls_items', '0005_remove_url_result'),
        ('urls_results', '0004_remove_result_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='url',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='urls_items.url', verbose_name='Url associé'),
        ),
    ]
