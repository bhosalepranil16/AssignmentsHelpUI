from django.shortcuts import render
from django.views import View

import requests

# Create your views here.

# BASE_URL = 'http://localhost:3000/api/'


BASE_URL = 'https://assignmentshelpbackend-pqbat.ondigitalocean.app/api/'


class HomeView(View):
    def get(self, request):
        return render(request, 'Home/index.html')


class UniversityView(View):
    def get(self, request):
        response = requests.get(f'{BASE_URL}university/')
        response_data = response.json()
        return render(request, 'Home/universities.html', {
            'universities': response_data['data']['universities']
        })


class UniversityDetailView(View):
    def get(self, request, university_slug):
        response = requests.get(f'{BASE_URL}university/{university_slug}')
        response_data = response.json()
        return render(request, 'Home/university-detail.html', {
            'university': response_data['data']['university'],
            'courses': response_data['data']['courses']
        })


class CourseDetailView(View):
    def get(self, request, university_slug, course_slug):
        response = requests.get(f'{BASE_URL}course/{course_slug}')
        response_data = response.json()
        return render(request, 'Home/course-detail.html', {
            'course': response_data['data']['course'],
            'subjects': response_data['data']['subjects']
        })


class SubjectDetailView(View):
    def get(self, request, university_slug, course_slug, subject_slug):
        response = requests.get(f'{BASE_URL}subject/{subject_slug}')
        response_data = response.json()
        return render(request, 'Home/subject-detail.html', {
            'subject': response_data['data']['subject'],
            'assignments': response_data['data']['assignments'],
            'course': response_data['data']['course']
        })


class AssignmentDetailView(View):
    def get(self, request, university_slug, course_slug, subject_slug, assignment_slug):
        response = requests.get(f'{BASE_URL}assignment/{assignment_slug}')
        response_data = response.json()
        return render(request, 'Home/assignment-detail.html', {
            'assignment': response_data['data']['assignment'],
            'subject': response_data['data']['subject'],
            'course': response_data['data']['course'],
        })


class AboutUsView(View):
    def get(self, request):
        return render(request, 'Home/about-us.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'Home/contact-us.html')

    def post(self, request):
        response = requests.post(f'{BASE_URL}contact-us/', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        })
        print(response.status_code)
        return render(request, 'Home/contact-us.html')


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'Home/privacy-policy.html')


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'Home/terms-and-condition.html')
