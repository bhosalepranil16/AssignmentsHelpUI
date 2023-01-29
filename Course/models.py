from django.db import models

from College.models import CollegeModel
from University.models import UniversityModel


# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    university = models.ForeignKey(UniversityModel, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


