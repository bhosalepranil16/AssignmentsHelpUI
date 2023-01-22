from django.contrib import admin

from .models import UniversityModel


# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(UniversityModel, UniversityAdmin)
