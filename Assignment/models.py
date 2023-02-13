from django.contrib.auth.models import User
from django.db import models

from Subject.models import SubjectModel


# Create your models here.


class AssignmentModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    assignment_no = models.IntegerField()
    question = models.TextField()
    codes = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return self.name


class AssignmentCommentModel(models.Model):
    text = models.TextField()
    assignment = models.ForeignKey(AssignmentModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Assignment Comment'
        verbose_name_plural = 'Assignment Comments'
