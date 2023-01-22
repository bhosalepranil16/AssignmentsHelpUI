# Generated by Django 4.1.5 on 2023-01-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=10)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colleges', to='University.universitymodel')),
            ],
            options={
                'verbose_name': 'College',
                'verbose_name_plural': 'Colleges',
            },
        ),
    ]
