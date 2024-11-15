# Generated by Django 4.1.5 on 2023-01-29 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('subject_code', models.CharField(max_length=10, unique=True)),
                ('short_name', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.coursemodel')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
    ]
