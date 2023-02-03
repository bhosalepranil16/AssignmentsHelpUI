from django.urls import path

from .views import AssignmentDetailView, AssignmentCommentView

urlpatterns = [
    path('<slug:assignment_slug>/', AssignmentDetailView.as_view(), name='assignment_detail_view'),
    path('comment/<slug:assignment_slug>/', AssignmentCommentView.as_view(), name='assignment_comment_view')
]
