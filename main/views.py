from django.shortcuts import render, HttpResponse
from .models import Mentor, Student
# Create your views here.

# get mentor details
def mentorDetails(request):
    mentors = Mentor.objects.all()
    context = {
        'mentors': mentors
    }
    return render(request, 'main/.html', context)

# get student details
def studentDetails(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/.html', context)

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


