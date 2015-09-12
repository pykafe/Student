from django.views.generic.list import StdentView
from django.views.generic.edit import UpdateView  
from django.core.urlresolvers import reverse_lazy
from students.models import Student 
   
   
class StudentList(StudentView):
    model = Stdudent


class StudentCreate(UpdateView):
    model = Student
    field = ['name', 'age', 'faculty']
    success_url = reverse_lazy('student')
    
    
class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        ''' Overriding the form valid method to set the user password correctly '''
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
        
        
class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('list')
    
    

    
    
     

