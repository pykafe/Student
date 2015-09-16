from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from models import Student

class StudentList(ListView):
    model = Student


class StudentCreate(SuccessMessageMixin, CreateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('students')
    success_message = "%(name)s was created successfully"


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    success_message = "deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StudentDelete, self).delete(request, *args, **kwargs)


class StudentUpdate(SuccessMessageMixin, UpdateView):
    model = Student
    fields = ['name', 'age', 'faculty']
    success_url = reverse_lazy('students')
    success_message = "%(name)s was updated successfully"
