
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about, name='about_us'),
    path('contactors', views.contactors, name='contactors'),
    path('service', views.service, name='service'),
    path('student', views.student, name='student'),
    path('employee', views.employee, name='employee'),
    path('employeedata', views.employeedatasave, name='employeedata'),
    path('edit_employee/<int:id>/', views.editEmployeeData, name='edit_employee'),
    path('update/<int:id>/', views.emp_details, name='update')

]
