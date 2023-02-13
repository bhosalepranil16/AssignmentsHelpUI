from django.contrib import admin

from .models import CourseModel


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'university')
    list_filter = ('university',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(CourseModel, CourseAdmin)
