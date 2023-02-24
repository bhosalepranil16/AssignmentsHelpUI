from django.shortcuts import render
from django.views import View

from .models import SubjectModel, DocumentModel


# Create your views here.
class SubjectDetailView(View):
    def get(self, request, subject_slug):
        try:
            subject = SubjectModel.objects.get(slug=subject_slug)
            documents = subject.documentmodel_set.all().order_by('priority')
            assignments = subject.assignmentmodel_set.all().order_by('assignment_no')
            return render(request, 'Subject/subject-detail.html', {
                'subject': subject,
                'assignments': assignments,
                'documents': documents
            })
        except Exception as err:
            return render(request, 'Subject/subject-detail.html', {
                'subject': {},
                'assignments': [],
                'documents': [],
                'show_errors': True,
                'errors': str(err)
            })
