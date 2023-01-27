from django.urls import path

from .views import SignUpView, LoginView, LogoutView, ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profile_view'),
    path('sign-up/', SignUpView.as_view(), name='sign_up_view'),
    path('login/',  LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view')
]
