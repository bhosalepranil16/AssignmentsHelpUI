from django.contrib import admin

from .models import CourseModel, CollegeCourseModel, UniversityCourseModel


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CollegeCourseAdmin(admin.ModelAdmin):
    list_display = ('college', 'course', 'total_intake')
    list_filter = ('college',)


class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ('university', 'course')
    list_filter = ('university',)


admin.site.register(CourseModel, CourseAdmin)
admin.site.register(CollegeCourseModel, CollegeCourseAdmin)
admin.site.register(UniversityCourseModel, UniversityCourseAdmin)
