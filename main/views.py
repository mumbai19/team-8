<<<<<<< HEAD
from django.shortcuts import render, HttpResponse
from .models import Mentor, Student,Activity
from .forms import ActivityForm
=======
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Mentor, Student, Attendance, Evaluate, Saving, Activity
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
    return render(request, 'main/studentDetails.html', {'students': students})

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

def getAttendance(request):
    attendance = Attendance.objects.all()
    for i in attendance:
        i.name = Student.objects.get(student_id = i.student_id).student_name
        i.savings = Saving.objects.get(student_id = i.student_id).savings
        i.saving_date = Saving.objects.get(student_id = i.student_id).saving_date
    return render(request, 'main/Attendance.html', {'attendance': attendance})

def getAssessments(request):
    assessments = Evaluate.objects.all()
    for i in assessments:
        i.name = Student.objects.get(student_id = i.student_id).student_name
    return render(request, 'main/getAssessment.html', {'evaluate': assessments})

def addAssessment(request):
    if request.method == "POST":
        student_id = Student.objects.get(student_name=request.POST['student_name'])
        assess_name = request.POST['assess_name']
        assess_date = request.POST['assess_date']
        assess_level = request.POST['assess_level']
        mentor = Mentor.objects.get(mentor_name=request.POST['mentor'])

        evaluate = Evaluate(student_id=student_id, assess_name=assess_name, assess_date=assess_date, assess_level=assess_level, mentor_id=mentor)
        evaluate.save()
        evaluate = Evaluate.objects.all()

        for i in evaluate:
            i.name = Student.objects.get(student_id = i.student_id).student_name
        return render(request, 'main/getAssessment.html', {'evaluate': evaluate})
    evaluate = Evaluate.objects.all()
    for i in evaluate:
        i.name = Student.objects.get(student_id = i.student_id).student_name
    return render(request, 'main/getAssessment.html', {'evaluate': evaluate})

def updateStudentInfo(request):
    if request.method == "POST":
        student_name = request.POST['student_name']
        parent_name = request.POST['parent_name']
        phone_no = request.POST['phone_no']
        standard = request.POST['standard']
        address = request.POST['address']
        mentor = Mentor.objects.get(mentor_name=request.POST['mentor'])

        student = Student(student_name=student_name, parent_name=parent_name, phone_no=phone_no, standard=standard, address=address, mentor=mentor)
        student.save()
        students = Student.objects.all()
        return render(request, 'main/studentDetails.html', {'students': students})
    students = Student.objects.all()
    return render(request, 'main/studentDetails.html', {'students': students})

def updateform(request):
    return render(request, 'main/studentUpdate.html')

def activitySubmit(request):
    if request.method == "POST":
        act_name = request.POST['activity_name']
        act_des = request.POST['activity_description']
        the = request.POST['theme']
        mentor = Mentor.objects.get(mentor_name=request.POST['mentor'])
        order = Activity.objects.create(activity_name=act_name, activity_description=act_des, theme=the, mentor_id=mentor)
        activities = Activity.objects.all()
        for i in activities:
            i.name = Mentor.objects.get(mentor_id = i.mentor_id).mentor_name
        return render(request, 'main/activityreport.html', {'activities': activities})
    activities = Activity.objects.all()
    for i in activities:
        i.name = Mentor.objects.get(mentor_id = i.mentor_id).mentor_name
    return render(request, 'main/activityreport.html', {'activities': activities})

<<<<<<< HEAD
def getActivity(request):
    activities = Activity.objects.all()
    for i in activities:
        i.name = Mentor.objects.get(mentor_id = i.mentor_id).mentor_name
    return render(request, 'main/activityreport.html', {'activities': activities})
=======
>>>>>>> 298a84e3a376e3f281ae47fa81e3266f5bfaa506
>>>>>>> 0ba27a104efa0140c5ea90bcf31c13879689bea1
