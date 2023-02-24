from django.db import models

from Course.models import CourseModel


# Create your models here.


class SubjectModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    subject_code = models.CharField(max_length=10, unique=True)
    short_name = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.name


class CourseSubjectModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        verbose_name = 'Course Subject'
        verbose_name_plural = 'Course Subject'

    def __str__(self):
        return f'{self.course.name} {self.subject.name}'


class DocumentModel(models.Model):
    name = models.CharField(max_length=100)
    file_url = models.URLField(null=True)
    priority = models.IntegerField()
    subject = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.name
