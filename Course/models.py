from django.db import models

from College.models import CollegeModel
from University.models import UniversityModel


# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class CollegeCourseModel(models.Model):
    college = models.ForeignKey(CollegeModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    total_intake = models.IntegerField()

    class Meta:
        verbose_name = 'CollegeCourse'
        verbose_name_plural = 'CollegeCourses'


class UniversityCourseModel(models.Model):
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'UniversityCourse'
        verbose_name_plural = 'UniversityCourses'
