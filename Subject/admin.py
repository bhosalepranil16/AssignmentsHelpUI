from django.contrib import admin

from .models import SubjectModel


# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'subject_code', 'course', 'semester', 'year')
    list_filter = ('semester', 'year')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SubjectModel, SubjectAdmin)
