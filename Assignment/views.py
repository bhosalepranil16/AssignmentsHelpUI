from django.shortcuts import render
from django.views import View

from .models import AssignmentModel, AssignmentImageModel


# Create your views here.
class AssignmentDetailView(View):
    def get(self, request, assignment_slug):
        try:
            assignment = AssignmentModel.objects.get(slug=assignment_slug)
            subject = assignment.subject
            course = assignment.subject.course
            output_screenshots = assignment.assignmentimagemodel_set.all()
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': assignment,
                'subject': subject,
                'course': course,
                'output_screenshots': output_screenshots
            })
        except Exception as err:
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': {},
                'subject': {},
                'course': {},
                'output_screenshots': [],
                'show_errors': True,
                'errors': str(err)
            })
