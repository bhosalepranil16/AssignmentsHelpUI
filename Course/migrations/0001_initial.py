# Generated by Django 4.1.5 on 2023-01-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('University', '0001_initial'),
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='UniversityCourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.coursemodel')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='University.universitymodel')),
            ],
            options={
                'verbose_name': 'UniversityCourse',
                'verbose_name_plural': 'UniversityCourses',
            },
        ),
        migrations.CreateModel(
            name='CollegeCourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_intake', models.IntegerField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.collegemodel')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.coursemodel')),
            ],
            options={
                'verbose_name': 'CollegeCourse',
                'verbose_name_plural': 'CollegeCourses',
            },
        ),
    ]
