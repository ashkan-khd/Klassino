# Generated by Django 3.1 on 2020-10-24 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0003_assignedstudyperiod_historicalassignedstudyperiod'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistancepackage',
            name='description',
            field=models.TextField(default='a khafan assistance package', verbose_name='معرفی بسته مشاره'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalassistancepackage',
            name='description',
            field=models.TextField(default='a khafan assistance package', verbose_name='معرفی بسته مشاره'),
            preserve_default=False,
        ),
    ]
