from django.forms import ModelForm

from .models import ContactUsModel


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUsModel
        fields = '__all__'
        labels = {
            'name': 'Your Name',
            'email': 'Your Email Address',
            'message': 'Your Message Here'
        }
