# Generated by Django 3.1 on 2020-10-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20201019_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstudent',
            name='nationality_code',
            field=models.CharField(db_index=True, max_length=10, verbose_name='شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='شماره شناسنامه'),
        ),
    ]
