from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^students/$', views.studentDetails, name='students'),
    url(r'^attendance/$', views.getAttendance, name='attendance'),
    url(r'^assessments/$', views.getAssessments, name='assessments')
    # url(r'^stars/$', views.getStars, name='stars'),
]