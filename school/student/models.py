from django.db import models


class Student(models.Model):
    name = charField(max_length=15)
    age = IntegerField()
    faculty = charField(max_length=15)
