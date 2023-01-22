from django.contrib import admin

from .models import ContactUsModel


# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('email',)


admin.site.register(ContactUsModel, ContactUsAdmin)
