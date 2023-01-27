from django.shortcuts import render
from django.views import View

from .models import UniversityModel
from Course.models import UniversityCourseModel
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
            university_course = UniversityCourseModel.objects.filter(university__slug=university_slug)
            colleges = CollegeModel.objects.filter(university__slug=university_slug)
            courses = []
            university = {}
            for a in university_course:
                b = {
                    'name': a.course.name,
                    'slug': a.course.slug
                }
                university = {
                    'name': a.university.name,
                    'slug': a.university.slug,
                    'short_name': a.university.short_name
                }
                courses.append(b)
            return render(request, 'University/university-detail.html', {
                'university': university,
                'courses': courses,
                'colleges': colleges
            })
        except Exception as err:
            return render(request, 'University/university-detail.html', {
                'university': {},
                'courses': [],
                'colleges': [],
                'show_errors': True,
                'errors': str(err)
            })
