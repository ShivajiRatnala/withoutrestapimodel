from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    cls=models.CharField(max_length=10)
    school=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)