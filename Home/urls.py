from django.urls import path

from .views import HomeView, AboutUsView, PrivacyPolicyView, TermsAndConditionView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('about-us/', AboutUsView.as_view(), name='about_us_view'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy_view'),
    path('terms-and-conditions/', TermsAndConditionView.as_view(), name='terms_and_condition_view')
]
