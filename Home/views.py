from django.shortcuts import render
from django.views import View

from University.models import UniversityModel
from Course.models import CourseModel


# Create your views here.


class HomeView(View):
    def get(self, request):
        universities = UniversityModel.objects.all()
        courses = CourseModel.objects.all()
        return render(request, 'Home/index.html', {
            'universities': universities,
            'courses': courses
        })


class AboutUsView(View):
    def get(self, request):
        return render(request, 'Home/about-us.html')


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'Home/privacy-policy.html')


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'Home/terms-and-condition.html')


class GoogleSearchConsoleView(View):
    def get(self, request):
        return render(request, 'Home/google2f18d2468a4ed341.html')


class SitemapView(View):
    def get(self, request):
        return render(request, 'Home/sitemap.xml')
