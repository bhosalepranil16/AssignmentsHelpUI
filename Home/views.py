from django.shortcuts import render
from django.views import View


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'Home/index.html')


class AboutUsView(View):
    def get(self, request):
        return render(request, 'Home/about-us.html')


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'Home/privacy-policy.html')


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'Home/terms-and-condition.html')
