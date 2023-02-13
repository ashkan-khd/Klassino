# Generated by Django 3.1 on 2020-10-16 22:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discounting', '0003_auto_20201016_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalassistancediscount',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalassistancediscount',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalcoursediscount',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalcoursediscount',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaldiscount',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان پایان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaldiscount',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان شروع'),
            preserve_default=False,
        ),
    ]