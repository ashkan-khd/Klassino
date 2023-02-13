# Generated by Django 3.1 on 2020-10-10 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_student'),
        ('introducing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherIntroductionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='لینک فیلم')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='introduction_videos', to='user.teacher', verbose_name='استاد')),
            ],
            options={
                'verbose_name': 'فیلم معرفی استاد',
                'verbose_name_plural': 'فیلم\u200cهای معرفی استاد',
            },
        ),
    ]