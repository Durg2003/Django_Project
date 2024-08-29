from django.contrib import admin
from SVKM.models import Question, Department, Employee
# Register your models here.
#every py file is model file and whenever access from one py file to another py file we used import..

admin.site.register(Question)
admin.site.register(Department)
admin.site.register(Employee)