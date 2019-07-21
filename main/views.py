from django.shortcuts import render, HttpResponse
from .models import Mentor, Student,Activity
from .forms import ActivityForm
# Create your views here.

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

