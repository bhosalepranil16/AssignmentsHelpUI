from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from django.views import View

from .forms import SignUpForm, LoginForm
from Assignment.models import AssignmentModel


# Create your views here.

class SignUpView(View):
    def get(self, request):
        try:
            sign_up_form = SignUpForm()
            if request.user.is_authenticated:
                return redirect(reverse('home_view'))
            return render(request, 'Profile/sign-up.html', {
                'sign_up_form': sign_up_form
            })
        except Exception:
            return render(request, 'Profile/sign-up.html', {
                'sign_up_form': sign_up_form
            })

    def post(self, request):
        try:
            sign_up_form = SignUpForm(request.POST)
            if request.user.is_authenticated:
                return redirect(reverse('home_view'))
            if sign_up_form.is_valid():
                email = sign_up_form.cleaned_data.get('email')
                password_first = sign_up_form.cleaned_data.get('password_first')
                password_second = sign_up_form.cleaned_data.get('password_second')
                if password_first != password_second:
                    raise ValidationError('Both Passwords Should Match!')
                user = User.objects.create_user(username=email, email=email, password=password_first)
                user.save()
                user = authenticate(request, username=email, password=password_first)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('home_view'))
            return render(request, 'Profile/sign-up.html', {
                'sign_up_form': sign_up_form
            })
        except Exception as err:
            return render(request, 'Profile/sign-up.html', {
                'sign_up_form': sign_up_form,
                'show_errors': True,
                'errors': str(err)
            })


class LoginView(View):
    def get(self, request):
        try:
            login_form = LoginForm()
            if request.user.is_authenticated:
                return redirect(reverse('home_view'))
            return render(request, 'Profile/login.html', {
                'login_form': login_form
            })
        except Exception as err:
            return render(request, 'Profile/login.html', {
                'login_form': login_form,
                'show_errors': True,
                'errors': str(err)
            })

    def post(self, request):
        try:
            login_form = LoginForm(request.POST)
            if request.user.is_authenticated:
                return redirect(reverse('home_view'))
            if login_form.is_valid():
                email = login_form.cleaned_data.get('email')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('home_view'))
                else:
                    raise ValidationError('Invalid Credentials')
            return render(request, 'Profile/login.html', {
                'login_form': login_form
            })
        except Exception as err:
            return render(request, 'Profile/login.html', {
                'login_form': login_form,
                'show_errors': True,
                'errors': str(err)
            })


class LogoutView(View):
    def get(self, request):
        try:
            logout(request)
            return redirect(reverse('home_view'))
        except Exception:
            return redirect(reverse('home_view'))


class ProfileView(View):
    def get(self, request):
        try:
            if not request.user.is_authenticated:
                return redirect(reverse('login_view'))
            else:
                user = request.user
                assignments = AssignmentModel.objects.filter(author_id=user.id)
                return render(request, 'Profile/profile.html', {
                    'assignments': assignments
                })
        except Exception:
            return render(request, 'Profile/profile.html', {
                'assignments': []
            })
