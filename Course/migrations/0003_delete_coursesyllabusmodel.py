# Generated by Django 4.1.5 on 2023-02-24 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_coursesyllabusmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseSyllabusModel',
        ),
    ]
