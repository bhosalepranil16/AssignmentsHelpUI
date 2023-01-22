from django.shortcuts import render
from django.views import View

from University.models import UniversityModel
from Course.models import CourseModel, UniversityCourseModel
from College.models import CollegeModel
from Subject.models import SubjectModel
from Assignment.models import AssignmentModel
from ContactUs.models import ContactUsModel


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'Home/index.html')


class UniversityView(View):
    def get(self, request):
        try:
            universities = UniversityModel.objects.all()
            return render(request, 'Home/universities.html', {
                'universities': universities
            })
        except Exception:
            return render(request, 'Home/universities.html', {
                'universities': []
            })


class UniversityDetailView(View):
    def get(self, request, university_slug):
        try:
            university_course = UniversityCourseModel.objects.filter(university__slug=university_slug)
            colleges = CollegeModel.objects.filter(university__slug=university_slug)
            courses = []
            university = {}
            for a in university_course:
                b = {
                    'name': a.course.name,
                    'slug': a.course.slug
                }
                university = {
                    'name': a.university.name,
                    'slug': a.university.slug,
                    'short_name': a.university.short_name
                }
                courses.append(b)
            return render(request, 'Home/university-detail.html', {
                'university': university,
                'courses': courses,
                'colleges': colleges
            })
        except Exception:
            return render(request, 'Home/university-detail.html', {
                'university': {},
                'courses': [],
                'colleges': []
            })


class CourseDetailView(View):
    def get(self, request, university_slug, course_slug):
        try:
            course = CourseModel.objects.get(slug=course_slug)
            subjects = SubjectModel.objects.filter(course__slug=course_slug).order_by('semester')
            return render(request, 'Home/course-detail.html', {
                'course': course,
                'subjects': subjects
            })
        except Exception:
            return render(request, 'Home/course-detail.html', {
                'course': {},
                'subjects': []
            })


class SubjectDetailView(View):
    def get(self, request, university_slug, course_slug, subject_slug):
        try:
            subject = SubjectModel.objects.get(slug=subject_slug)
            assignments = AssignmentModel.objects.filter(subject__slug=subject_slug)
            course = subject.course
            return render(request, 'Home/subject-detail.html', {
                'subject': subject,
                'assignments': assignments,
                'course': course
            })
        except Exception:
            return render(request, 'Home/subject-detail.html', {
                'subject': {},
                'assignments': [],
                'course': {}
            })


class AssignmentDetailView(View):
    def get(self, request, university_slug, course_slug, subject_slug, assignment_slug):
        try:
            assignment = AssignmentModel.objects.get(slug=assignment_slug)
            subject = assignment.subject
            course = assignment.subject.course
            return render(request, 'Home/assignment-detail.html', {
                'assignment': assignment,
                'subject': subject,
                'course': course,
            })
        except Exception:
            return render(request, 'Home/assignment-detail.html', {
                'assignment': {},
                'subject': {},
                'course': {},
            })


class AboutUsView(View):
    def get(self, request):
        return render(request, 'Home/about-us.html')


class ContactUsView(View):
    def get(self, request):
        return render(request, 'Home/contact-us.html')

    def post(self, request):
        try:
            contact_us = ContactUsModel(name=request.POST['name'], email=request.POST['email'],
                                        message=request.POST['message'])
            contact_us.save()
            return render(request, 'Home/contact-us.html')
        except Exception:
            return render(request, 'Home/contact-us.html')


class PrivacyPolicyView(View):
    def get(self, request):
        return render(request, 'Home/privacy-policy.html')


class TermsAndConditionView(View):
    def get(self, request):
        return render(request, 'Home/terms-and-condition.html')
