# Generated by Django 3.1 on 2020-11-23 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teaching', '0007_merge_20201103_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('skyroom_login_url', models.URLField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='teaching.coursesession')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='teaching.coursesubscription')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalSessionAttendance',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('skyroom_login_url', models.URLField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='teaching.coursesession')),
                ('subscription', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='teaching.coursesubscription')),
            ],
            options={
                'verbose_name': 'historical session attendance',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
