from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^students/$', views.studentDetails, name='students'),
    url(r'^attendance/$', views.getAttendance, name='attendance'),
    url(r'^assessments/$', views.getAssessments, name='assessments'),
    url(r'^addassessment/$', views.addAssessment, name='addassessment'),
    url(r'^addtassessment/$', views.addtAssessment, name='addtassessment'),
    url(r'^studentupdate/$', views.updateStudentInfo, name='studentupdate'),
    url(r'^studentsform/$', views.updateform, name='studentsform'),
    url(r'^addtactivity/$', views.activitytSubmit, name='addtactivity'),
    url(r'^addactivity/$', views.activitySubmit, name='addactivity'),
    url(r'^getactivity/$', views.getActivity, name='getactivity')
    # url(r'^stars/$', views.getStars, name='stars'),
]