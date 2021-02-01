# Generated by Django 3.1.3 on 2021-02-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urls_results', '0004_remove_result_url'),
        ('urls_items', '0003_remove_url_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='result',
            field=models.ForeignKey(db_index=False, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_results.result', verbose_name='Résultat'),
        ),
    ]