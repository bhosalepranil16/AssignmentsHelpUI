from django.shortcuts import render
from django.views import View

from .models import UniversityModel
from Course.models import CourseModel
from College.models import CollegeModel


# Create your views here.

class UniversityView(View):
    def get(self, request):
        try:
            universities = UniversityModel.objects.all()
            return render(request, 'University/universities.html', {
                'universities': universities
            })
        except Exception as err:
            return render(request, 'University/universities.html', {
                'universities': [],
                'show_errors': True,
                'errors': str(err)
            })


class UniversityDetailView(View):
    def get(self, request, university_slug):
        try:
            university = UniversityModel.objects.get(slug=university_slug)
            courses = CourseModel.objects.filter(university=university)
            return render(request, 'University/university-detail.html', {
                'university': university,
                'courses': courses
            })
        except Exception as err:
            return render(request, 'University/university-detail.html', {
                'university': {},
                'courses': [],
                'show_errors': True,
                'errors': str(err)
            })
