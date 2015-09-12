from django.views.generic.list import StdentView
   
   
   
class StudentList(StudentView):
    model = Stdudent


class StudentCreate(CreatetView):
    model = Student
    field = ['name', 'age', 'faculty']
    success_url = reverse_lazy('student')
    
    
     

