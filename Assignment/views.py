from django.shortcuts import render, redirect, reverse
from django.views import View

from .models import AssignmentModel, AssignmentCommentModel


# Create your views here.
class AssignmentDetailView(View):
    def get(self, request, assignment_slug):
        try:
            assignment = AssignmentModel.objects.get(slug=assignment_slug)
            subject = assignment.subject
            course = assignment.subject.course
            output_screenshots = assignment.assignmentimagemodel_set.all()
            comments = assignment.assignmentcommentmodel_set.all().order_by('-created_at')
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': assignment,
                'subject': subject,
                'course': course,
                'output_screenshots': output_screenshots,
                'comments': comments
            })
        except Exception as err:
            print(str(err))
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': {},
                'subject': {},
                'course': {},
                'output_screenshots': [],
                'comments': [],
                'show_errors': True,
                'errors': str(err)
            })


class AssignmentCommentView(View):
    def post(self, request, assignment_slug):
        try:
            if not request.user.is_authenticated:
                return redirect(reverse('login_view'))
            assignment = AssignmentModel.objects.get(slug=assignment_slug)
            comment = AssignmentCommentModel(text=request.POST['text'], assignment=assignment, author=request.user)
            comment.save()
            return redirect(reverse('assignment_detail_view', args=[assignment_slug]))
        except Exception as err:
            print(err)
            return redirect(reverse('assignment_detail_view', args=[assignment_slug]))
