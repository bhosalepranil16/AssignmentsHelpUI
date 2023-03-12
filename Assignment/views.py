import requests

from django.shortcuts import render, redirect, reverse
from django.views import View

from .models import AssignmentModel, AssignmentCommentModel


# Create your views here.
class AssignmentDetailView(View):
    def get(self, request, assignment_slug):
        try:
            assignment = AssignmentModel.objects.get(slug=assignment_slug)
            subject = assignment.subject
            comments = assignment.assignmentcommentmodel_set.all().order_by('-created_at')
            if len(assignment.codes) > 0:
                gist_id = assignment.codes[40:-3]
                content = requests.get(f'https://api.github.com/gists/{gist_id}')
                content = content.json()
                files_data = list(content['files'].values())
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': assignment,
                'subject': subject,
                'comments': comments,
                'files_data': files_data
            })
        except Exception as err:
            print(str(err))
            return render(request, 'Assignment/assignment-detail.html', {
                'assignment': {},
                'subject': {},
                'comments': [],
                'show_errors': True,
                'files_data': [],
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
