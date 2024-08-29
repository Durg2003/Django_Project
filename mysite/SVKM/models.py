from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    noOfQuestion = models.IntegerField()
    put_date = models.DateTimeField("date Published")

class Department(models.Model):
    department_text = models.CharField(max_length=200)
    noOfPeopleInDepartment = models.IntegerField()
    headofDepartmentName = models.CharField(max_length=100)
    departmentPhoneno = models.IntegerField()
    departmentEmailId = models.EmailField()

class Employee(models.Model):
    employeeName = models.CharField(max_length=200)
    employeeDesignation = models.CharField(max_length=100)
    employeeSalary = models.IntegerField()

    def __str__(self):
        return self.employeeName