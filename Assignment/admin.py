from django.contrib import admin

from .models import AssignmentModel, AssignmentImageModel


# Register your models here.


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignment_no', 'subject', 'author')
    list_filter = ('subject', 'author')
    prepopulated_fields = {'slug': ('name',)}


class AssignmentImagAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'image')
    list_filter = ('assignment',)


admin.site.register(AssignmentModel, AssignmentAdmin)
admin.site.register(AssignmentImageModel, AssignmentImagAdmin)
