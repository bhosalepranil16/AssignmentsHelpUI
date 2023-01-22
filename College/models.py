from django.db import models

from University.models import UniversityModel


# Create your models here.

class CollegeModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10)
    university = models.ForeignKey(UniversityModel, related_name='colleges', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'Colleges'

    def __str__(self):
        return self.name
