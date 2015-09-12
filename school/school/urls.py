from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.StudentList.as_view(), name='students'),
    
]
