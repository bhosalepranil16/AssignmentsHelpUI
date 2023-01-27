from django.urls import path

from .views import SubjectDetailView

urlpatterns = [
    path('<slug:subject_slug>/', SubjectDetailView.as_view(), name='subject_detail_view')
]
