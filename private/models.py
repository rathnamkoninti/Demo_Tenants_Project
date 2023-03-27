from django.db import models

# Create your models here.
class PublicTable1(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
  
class College(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)

class Student(models.Model):
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
