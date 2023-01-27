from django.shortcuts import render
from django.views import View

from .models import CourseModel
from Subject.models import SubjectModel


# Create your views here.

class CourseDetailView(View):
    def get(self, request, course_slug):
        try:
            course = CourseModel.objects.get(slug=course_slug)
            subjects = SubjectModel.objects.filter(course__slug=course_slug).order_by('semester')
            return render(request, 'Course/course-detail.html', {
                'course': course,
                'subjects': subjects
            })
        except Exception as err:
            return render(request, 'Course/course-detail.html', {
                'course': {},
                'subjects': [],
                'show_errors': True,
                'errors': str(err)
            })
