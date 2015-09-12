from django.conf.urls import include, url
from django.contrbi import admin 
from student.views import SrudentList

urlpatterns = [
   url(r'^$', login_required(views.Student.as_view()), name='list'),
   url(r'^create/(?P<pk>\d+)/$', login_required(views.StudentCreate.as_view()), name='create'),
   url(r'^delete/(?P<pk>\d+)/$', login_required(views.StudentDelete.as_view()), name='delete'),
   url(r'^update/(?P<pk>\d+)/$', login_required(views.StudentUpdate.as_view()), name='update'),
]
