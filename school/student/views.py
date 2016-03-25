from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, ModelFormMixin 
from django.core.urlresolvers import reverse_lazy
from student.models import Student 
   
   
class StudentList(ListView):
    model = Student
    
    
class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('list')
    
    
class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('list')

    
        
        
class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('list')
    
    

    
    
     

