from django.urls import path

from .views import UniversityView, UniversityDetailView

urlpatterns = [
    path('', UniversityView.as_view(), name='university_view'),
    path('<slug:university_slug>/', UniversityDetailView.as_view(), name='university_detail_view')
]
