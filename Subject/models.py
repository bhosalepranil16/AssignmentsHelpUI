from django.db import models

from Course.models import CourseModel


# Create your models here.


class SubjectModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    subject_code = models.CharField(max_length=10, unique=True)
    short_name = models.CharField(max_length=10)
    year = models.IntegerField()
    semester = models.IntegerField()
    description = models.TextField(blank=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name
