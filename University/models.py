from django.db import models


# Create your models here.

class UniversityModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_name = models.CharField(max_length=10)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'

    def __str__(self):
        return self.name
