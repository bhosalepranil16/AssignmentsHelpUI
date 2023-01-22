from django.contrib import admin

from .models import CollegeModel


# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'university')
    list_filter = ('university',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CollegeModel, CollegeAdmin)
