# Generated by Django 3.1 on 2020-10-24 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_auto_20201019_2323'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ تراکنش')),
                ('description', models.TextField(verbose_name='توضیحات تراکنش')),
                ('transaction_time', models.DateField(verbose_name='تاریخ تراکنش')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='user.student', verbose_name='تراکنشگر')),
            ],
        ),
        migrations.CreateModel(
            name='ManualTransaction',
            fields=[
                ('primetransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financial.primetransaction')),
            ],
            options={
                'verbose_name': 'تراکنش دستی',
                'verbose_name_plural': 'تراکنش های دستی',
            },
            bases=('financial.primetransaction',),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('primetransaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financial.primetransaction')),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش ها',
            },
            bases=('financial.primetransaction',),
        ),
        migrations.CreateModel(
            name='HistoricalTransaction',
            fields=[
                ('primetransaction_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='financial.primetransaction')),
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ تراکنش')),
                ('description', models.TextField(verbose_name='توضیحات تراکنش')),
                ('transaction_time', models.DateField(verbose_name='تاریخ تراکنش')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='تراکنشگر')),
            ],
            options={
                'verbose_name': 'historical تراکنش',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPrimeTransaction',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ تراکنش')),
                ('description', models.TextField(verbose_name='توضیحات تراکنش')),
                ('transaction_time', models.DateField(verbose_name='تاریخ تراکنش')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='تراکنشگر')),
            ],
            options={
                'verbose_name': 'historical prime transaction',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalManualTransaction',
            fields=[
                ('primetransaction_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='financial.primetransaction')),
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('amount', models.BigIntegerField(verbose_name='مبلغ تراکنش')),
                ('description', models.TextField(verbose_name='توضیحات تراکنش')),
                ('transaction_time', models.DateField(verbose_name='تاریخ تراکنش')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='تراکنشگر')),
            ],
            options={
                'verbose_name': 'historical تراکنش دستی',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
