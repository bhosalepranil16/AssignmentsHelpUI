from django.urls import path

from .views import AssignmentDetailView

urlpatterns = [
    path('<slug:assignment_slug>/', AssignmentDetailView.as_view(), name='assignment_detail_view')
]
