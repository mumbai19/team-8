<<<<<<< HEAD
from django.shortcuts import render, HttpResponse
from .models import Mentor, Student,Activity
from .forms import ActivityForm
=======
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Mentor, Student, Attendance, Evaluate
from django.contrib.auth.models import User
>>>>>>> 298a84e3a376e3f281ae47fa81e3266f5bfaa506
# Create your views here.

# get index page
def index(request):
    return render(request, 'main/base_visitor.html')

# get index page
def dashboard(request):
    return render(request, 'main/dashboard.html')

# get mentor details
# def mentorDetails(request):
#     mentors = Mentor.objects.all()
#     context = {
#         'mentors': mentors
#     }
#     return render(request, 'main/index.html', context)
#
# # get student details
# def studentDetails(request):
#     students = Student.objects.all()
#     context = {
#         'students': students
#     }
#     return render(request, 'main/.html', context)
#
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return render(request, 'main/.html', {'albums': {}})
#             else:
#                 return render(request, 'main/.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'main/.html', {'error_message': 'Invalid login'})
#     return render(request, 'main/.html')

<<<<<<< HEAD
def activitySubmit(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        resource = form.save(commit=False)
        activityID = form.cleaned_data['activity_id']
        themeName = form.cleaned_data['theme']
        activityName = form.cleaned_data['activity_name']
        activityDescription = form.cleaned_data['activity_description']
        mentorID = form.cleaned_data['mentor_id']
        resource.save()
        return render(request, 'main/ActAssessment.html', {'resource': resource})

=======
# get student details
def studentDetails(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/studentDetails.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'main/.html', {'albums': {}})
            else:
                return render(request, 'main/.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'main/.html', {'error_message': 'Invalid login'})
    return render(request, 'main/.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User(username = username, password = password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'main/.html')
    return render(request, 'main/.html')

def getAttendance(request, student_id):
    attendance = Attendance.objects.get(student_id=student_id)
    context = {
        'attendance': attendance
    }
    return render(request, 'main/.html', context)

def getAssessments(request, student_id):
    assessments = Evaluate.objects.get(student_id=student_id)
    context = {
        'assessments': assessments
    }
    return render(request, 'main/.html', context)

def updateStudentInfo(request, student_id):
    if request.method == "POST":
        student_name = request.POST['student_name']
        parent_name = request.POST['parent_name']
        phone_no = request.POST['phone_no']
        standard = request.POST['standard']
        address = request.POST['address']
        mentor = request.POST['mentor']

        Student.objects.get(student_id=student_id).update(student_name=student_name, parent_name=parent_name, phone_no=phone_no, standard=standard, address=address, mentor=mentor)
        return render(request, 'main/.html')
    return render(request, 'main/.html')

>>>>>>> 298a84e3a376e3f281ae47fa81e3266f5bfaa506
