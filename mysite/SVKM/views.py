from django.shortcuts import render, HttpResponse
from SVKM.models import Employee

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    context={
        'name' : 'Durgesh',
        'b_name' : 'IT',
        'c_name' : 'Dhule',
        'roll_no' : 50,
        'student_id' : 14004210050
    }
    return render(request, 'about.html', context)

def contactors(request):
    return render(request, 'contactors.html')

def service(request):
    return render(request, 'service.html')

def student(request):
    var1 = request.POST['fname']
    var2 = int(request.POST['rollno'])
    var3 = request.POST['lname']
    var4 = int(request.POST['id'])

    var5 = int(request.POST['phy'])
    var6 = int(request.POST['chem'])
    var7 = int(request.POST['math'])
    var8 = int(request.POST['eng'])
    var9 = int(request.POST['hindi'])

    total = var5 + var6 + var7 + var8 + var9
    percentage = total/5 

    if percentage > 40:
        Status = 'Pass'
    elif percentage < 40:
        Status = 'Fail'
    
    if 80 <= percentage <= 90:
        Grade = 'A' 
    elif 60 <= percentage <= 80:
        Grade = 'B'
    elif 40 <= percentage <+ 60:
        Grade = 'C'
    elif percentage < 40:
        Grade = 'D'


    res = {
        'name' : var1,
        'name' : var2,
        'name' : var3,
        'name' : var4,
        'name' : var5,
        'name' : var6,
        'name' : var7,
        'name' : var8,
        'name' : var9,
        't' : total,
        'perc' : percentage,
        'st' : Status,
        'grade' : Grade,
    }

    return render(request, 'result.html', res)


def employee(request):
    emp_obj = Employee.objects.all()
    return render(request, 'employee.html',{'emp_obj' : emp_obj})

def employeedatasave(request):
    employee_name = request.POST['fname']
    employee_designation = request.POST['lname']
    employee_salary = int(request.POST['Salary'])

    obj = Employee(employeeName=employee_name, employeeDesignation=employee_designation,employeeSalary=employee_salary)
    obj.save()
    msg = 'Data Save Successfully'
    emp_obj = Employee.objects.all()
    return render(request, 'employee.html', {'emp_obj' : emp_obj})

def editEmployeeData(request, id):
    emp_obj_edit = Employee.objects.get(id = id)
    return render(request, 'editemployee.html', {'emp_obj_edit' : emp_obj_edit})

def emp_details(request, id):
    if request.method == 'POST':
        emp_details= Employee.objects.get(id=id)
        emp_details.employeeName=request.POST['fname']
        emp_details.employeeDesignation=request.POST['lname']
        emp_details.employeeSalary=request.POST['Salary']
        emp_details.save()

        emp_obj = Employee.objects.all()
        return render(request, 'editemployee.html', {'msg':"Successfully Updated", 'emp_obj_edit': emp_details,'emp_obj' : emp_obj})
    else:
        return render('edit_employee', id=id)