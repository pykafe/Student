from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from models import Student
   
class StudentList(ListView):
    model = Student


class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('students')


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('students')

    
    
     

