# Generated by Django 3.1 on 2020-10-15 20:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20201015_0009'),
        ('teaching', '0004_auto_20201014_2241'),
        ('mentoring', '0003_assignedstudyperiod_historicalassignedstudyperiod'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('code', models.CharField(max_length=5, verbose_name='کد')),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student', verbose_name='خریدار کد تخفیف')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDiscount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('code', models.CharField(max_length=5, verbose_name='کد')),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='خریدار کد تخفیف')),
            ],
            options={
                'verbose_name': 'historical discount',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCourseDiscount',
            fields=[
                ('discount_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='discounting.discount')),
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('code', models.CharField(max_length=5, verbose_name='کد')),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('course', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='teaching.course', verbose_name='دوره')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='خریدار کد تخفیف')),
            ],
            options={
                'verbose_name': 'historical course discount',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAssistanceDiscount',
            fields=[
                ('discount_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='discounting.discount')),
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ ایجاد')),
                ('updated', models.DateTimeField(blank=True, editable=False, verbose_name='تاریخ آخرین ویرایش')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
                ('code', models.CharField(max_length=5, verbose_name='کد')),
                ('percentage', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assistance', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mentoring.assistancepackage', verbose_name='مشاوره')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user.student', verbose_name='خریدار کد تخفیف')),
            ],
            options={
                'verbose_name': 'historical assistance discount',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='CourseDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='discounting.discount')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='teaching.course', verbose_name='دوره')),
            ],
            options={
                'abstract': False,
            },
            bases=('discounting.discount',),
        ),
        migrations.CreateModel(
            name='AssistanceDiscount',
            fields=[
                ('discount_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='discounting.discount')),
                ('assistance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='mentoring.assistancepackage', verbose_name='مشاوره')),
            ],
            options={
                'abstract': False,
            },
            bases=('discounting.discount',),
        ),
    ]
