from django.shortcuts import render
from django.views import View

from .models import SubjectModel
from Assignment.models import AssignmentModel


# Create your views here.
class SubjectDetailView(View):
    def get(self, request, subject_slug):
        try:
            subject = SubjectModel.objects.get(slug=subject_slug)
            assignments = subject.assignmentmodel_set.all()
            course = subject.course
            return render(request, 'Subject/subject-detail.html', {
                'subject': subject,
                'assignments': assignments,
                'course': course
            })
        except Exception as err:
            return render(request, 'Subject/subject-detail.html', {
                'subject': {},
                'assignments': [],
                'course': {},
                'show_errors': True,
                'errors': str(err)
            })
