# Generated by Django 3.1 on 2020-10-10 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='زمان شروع جلسه')),
                ('end_time', models.DateTimeField(verbose_name='زمان پایان جلسه')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teaching.course')),
            ],
            options={
                'verbose_name': 'جلسه ی کلاس',
            },
        ),
    ]
