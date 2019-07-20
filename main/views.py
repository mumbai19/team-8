from django.shortcuts import render, HttpResponse
from .models import Mentor
# Create your views here.

# get mentor details
def mentorDetails(request):
    mentors = Mentor.objects.all()


