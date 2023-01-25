from django.contrib import admin

from .models import AssignmentModel, TagModel


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignment_no', 'subject')
    list_filter = ('subject',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(AssignmentModel, AssignmentAdmin)
admin.site.register(TagModel, TagAdmin)
