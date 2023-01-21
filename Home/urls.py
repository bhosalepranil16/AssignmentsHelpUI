from django.urls import path

from .views import HomeView, UniversityView, UniversityDetailView, CourseDetailView, SubjectDetailView, AssignmentDetailView, AboutUsView, ContactUsView, PrivacyPolicyView, TermsAndConditionView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('about-us/', AboutUsView.as_view(), name='about_us_view'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us_view'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy_view'),
    path('terms-and-conditions/', TermsAndConditionView.as_view(), name='terms_and_condition_view'),
    path('university/', UniversityView.as_view(), name='university_view'),
    path('university/<slug:university_slug>/', UniversityDetailView.as_view(), name='university_detail_view'),
    path('university/<slug:university_slug>/course/<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail_view'),
    path('university/<slug:university_slug>/course/<slug:course_slug>/subject/<slug:subject_slug>/', SubjectDetailView.as_view(),
         name='subject_detail_view'),
    path('university/<slug:university_slug>/course/<slug:course_slug>/subject/<slug:subject_slug>/assignment/<slug:assignment_slug>/',
         AssignmentDetailView.as_view(), name='assignment_detail_view')
]
