from django.shortcuts import render
from django.views import View

from .models import CourseModel


# Create your views here.

class CourseDetailView(View):
    def get(self, request, course_slug):
        try:
            course = CourseModel.objects.get(slug=course_slug)
            subjects = course.subjectmodel_set.all().order_by('semester')
            syllabuses = course.coursesyllabusmodel_set.all()
            return render(request, 'Course/course-detail.html', {
                'course': course,
                'subjects': subjects,
                'syllabuses': syllabuses
            })
        except Exception as err:
            return render(request, 'Course/course-detail.html', {
                'course': {},
                'subjects': [],
                'show_errors': True,
                'syllabuses': [],
                'errors': str(err)
            })
