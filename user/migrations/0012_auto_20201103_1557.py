# Generated by Django 3.1 on 2020-11-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20201103_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='historicalassistant',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='historicalstudent',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='historicalteacher',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='شماره تلفن'),
        ),
    ]
