from django.views.generic.list import ListView

from models import Student
   
class StudentList(ListView):
    model = Student

    
    
     

