from django.conf.urls import include, url
from django.contrib import admin 
import views 


urlpatterns = [
   url(r'^$', views.StudentList.as_view(), name='list'),
   url(r'^create/$', views.StudentCreate.as_view(), name='create'),
   url(r'^update/(?P<pk>\d+)/$', views.StudentUpdate.as_view(), name='update'),
   url(r'^delete/(?P<pk>\d+)/$', views.StudentDelete.as_view(), name='delete'),
]
