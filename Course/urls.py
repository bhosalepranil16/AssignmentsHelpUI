from django.urls import path

from .views import CourseDetailView

urlpatterns = [
    path('<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail_view')
]
