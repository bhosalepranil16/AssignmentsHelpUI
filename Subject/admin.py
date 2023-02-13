from django.contrib import admin

from .models import SubjectModel, CourseSubjectModel


# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'subject_code')
    prepopulated_fields = {'slug': ('name',)}


class CourseSubjectAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'year', 'semester')
    list_filter = ('course', 'subject', 'year', 'semester')


admin.site.register(SubjectModel, SubjectAdmin)
admin.site.register(CourseSubjectModel, CourseSubjectAdmin)
