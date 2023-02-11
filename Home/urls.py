from django.urls import path

from .views import HomeView, AboutUsView, PrivacyPolicyView, TermsAndConditionView, GoogleSearchConsoleView, SitemapView

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('about-us/', AboutUsView.as_view(), name='about_us_view'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy_view'),
    path('terms-and-conditions/', TermsAndConditionView.as_view(), name='terms_and_condition_view'),
    path('sitemap/', SitemapView.as_view(), name='sitemap_view'),
    path('google2f18d2468a4ed341.html', GoogleSearchConsoleView.as_view(), name='google_search_console_view')
]
