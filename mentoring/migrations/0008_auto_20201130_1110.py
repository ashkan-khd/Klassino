# Generated by Django 3.1 on 2020-11-30 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoring', '0007_auto_20201103_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assistancecourse',
            name='purchase_time',
        ),
        migrations.RemoveField(
            model_name='assistancecourse',
            name='transaction',
        ),
        migrations.RemoveField(
            model_name='historicalassistancecourse',
            name='purchase_time',
        ),
        migrations.RemoveField(
            model_name='historicalassistancecourse',
            name='transaction',
        ),
    ]