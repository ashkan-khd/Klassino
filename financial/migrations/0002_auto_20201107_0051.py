# Generated by Django 3.1 on 2020-11-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmanualtransaction',
            name='transaction_time',
            field=models.DateTimeField(verbose_name='تاریخ تراکنش'),
        ),
        migrations.AlterField(
            model_name='historicalprimetransaction',
            name='transaction_time',
            field=models.DateTimeField(verbose_name='تاریخ تراکنش'),
        ),
        migrations.AlterField(
            model_name='historicaltransaction',
            name='transaction_time',
            field=models.DateTimeField(verbose_name='تاریخ تراکنش'),
        ),
        migrations.AlterField(
            model_name='primetransaction',
            name='transaction_time',
            field=models.DateTimeField(verbose_name='تاریخ تراکنش'),
        ),
    ]
