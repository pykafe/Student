from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    faculty =models.CharField(max_length=35)
