from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.StudentList.as_view(), name='students'),
    url(r'^create$', views.StudentCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.StudentDelete.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)/$', views.StudentUpdate.as_view(), name='update'),
    
]
