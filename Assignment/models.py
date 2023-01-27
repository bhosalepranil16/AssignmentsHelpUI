from django.db import models
from django.contrib.postgres.fields import ArrayField

from Subject.models import SubjectModel


# Create your models here.


class AssignmentModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    assignment_no = models.IntegerField()
    question = models.TextField()
    codes = models.CharField(max_length=200)
    outputs = ArrayField(models.CharField(max_length=200))
    subject = models.ForeignKey(SubjectModel, related_name='assignments', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.name
