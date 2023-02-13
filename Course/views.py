from django.shortcuts import render
from django.views import View

from .models import CourseModel
from Subject.models import CourseSubjectModel


# Create your views here.

class CourseDetailView(View):
    def get(self, request, course_slug):
        try:
            course = CourseModel.objects.get(slug=course_slug)
            syllabuses = course.coursesyllabusmodel_set.all()
            course_subjects = CourseSubjectModel.objects.filter(course__slug=course_slug).order_by('semester')
            return render(request, 'Course/course-detail.html', {
                'course': course,
                'course_subjects': course_subjects,
                'syllabuses': syllabuses
            })
        except Exception as err:
            return render(request, 'Course/course-detail.html', {
                'course': {},
                'course_subjects': [],
                'show_errors': True,
                'syllabuses': [],
                'errors': str(err)
            })
