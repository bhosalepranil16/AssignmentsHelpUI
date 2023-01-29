from django.contrib import admin

from .models import CourseModel, CourseSyllabusModel


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'university')
    list_filter = ('university',)
    prepopulated_fields = {'slug': ('name',)}


class CourseSyllabusAdmin(admin.ModelAdmin):
    list_display = ('course', 'syllabus')
    list_filter = ('course',)


admin.site.register(CourseModel, CourseAdmin)
admin.site.register(CourseSyllabusModel, CourseSyllabusAdmin)
