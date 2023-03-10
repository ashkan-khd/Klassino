# Generated by Django 3.1 on 2020-10-16 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounting', '0004_auto_20201017_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='استفاده شده؟'),
        ),
        migrations.AddField(
            model_name='historicalassistancediscount',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='استفاده شده؟'),
        ),
        migrations.AddField(
            model_name='historicalcoursediscount',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='استفاده شده؟'),
        ),
        migrations.AddField(
            model_name='historicaldiscount',
            name='is_used',
            field=models.BooleanField(default=False, verbose_name='استفاده شده؟'),
        ),
    ]
