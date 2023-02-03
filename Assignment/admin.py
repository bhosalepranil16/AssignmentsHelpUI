from django.contrib import admin

from .models import AssignmentModel, AssignmentImageModel, AssignmentCommentModel


# Register your models here.


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'assignment_no', 'subject', 'author')
    list_filter = ('subject', 'author')
    prepopulated_fields = {'slug': ('name',)}


class AssignmentImagAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'image')
    list_filter = ('assignment',)


class AssignmentCommentAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'author')
    list_filter = ('assignment', 'author')


admin.site.register(AssignmentModel, AssignmentAdmin)
admin.site.register(AssignmentImageModel, AssignmentImagAdmin)
admin.site.register(AssignmentCommentModel, AssignmentCommentAdmin)
