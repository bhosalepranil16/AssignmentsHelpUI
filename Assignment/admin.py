from django.contrib import admin

from .models import AssignmentModel


# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignment_no', 'subject')
    list_filter = ('subject',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(AssignmentModel, AssignmentAdmin)
