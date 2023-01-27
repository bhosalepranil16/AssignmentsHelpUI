from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ContactUsForm


# Create your views here.
class ContactUsView(View):
    def get(self, request):
        try:
            contact_us_form = ContactUsForm()
            return render(request, 'ContactUs/contact-us.html', {
                'contact_us_form': contact_us_form
            })
        except Exception as err:
            return render(request, 'ContactUs/contact-us.html', {
                'contact_us_form': contact_us_form,
                'show_errors': True,
                'errors': str(err)
            })

    def post(self, request):
        try:
            contact_us_form = ContactUsForm(data=request.POST)
            if contact_us_form.is_valid():
                contact_us_form.save()
                return HttpResponseRedirect(reverse('home_view'))
            else:
                return render(request, 'ContactUs/contact-us.html', {
                    'contact_us_form': contact_us_form
                })
        except Exception as err:
            return render(request, 'ContactUs/contact-us.html', {
                'contact_us_form': contact_us_form,
                'show_errors': True,
                'errors': str(err)
            })
