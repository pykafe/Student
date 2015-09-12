from django.conf.urls import include, url
from django.contrbi import admin 
from student.views import SrudentList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('student.urls')),
]
