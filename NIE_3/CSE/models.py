from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    college_name = models.CharField(max_length=30)
    rollnumber = models.IntegerField()
    def __str__(self):
        return self.name
    


class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    def __str__(self):
        return self.emp_name


