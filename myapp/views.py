from django.forms import formset_factory
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee, Attendance
from .form import EmployeeForm, AttendanceForm

# Add Employee
def add_employee_view(request):
    today_date = timezone.now().date()
    all_employees = Employee.objects.all()
    today_attendance = Attendance.objects.filter(date=today_date)
    all_attendance = Attendance.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee Successfully Added')
            return redirect('/')
    else:
        form = EmployeeForm(label_suffix='')

    context = {
        'form': form,
        'all_employees': all_employees,
        'today_attendance': today_attendance,
        'all_attendance': all_attendance,
    }

    return render(request, 'employee.html', context)

# Update Employee
def update_employee_view(request, id):
    all_employees = Employee.objects.all()
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee, label_suffix='')
        if form.is_valid():
            form.save()
            messages.info(request, f'Employee Successfully updated')
            return redirect('/')
    else:
        form = EmployeeForm(instance=employee, label_suffix='')
    context = {
        'form': form,
        'employee': employee,
        'all_employees': all_employees,
    }
    return render(request, 'employee.html', context)

# Delete Employee
def delete_employee_view(request,id):
  try:
    employee = Employee.objects.get(id=id)
    employee.delete()
    messages.error(request, f'Employee Successfully deleted')
    return redirect('/')
  except Employee.DoesNotExist:
    messages.error(request, f'Employee not exist')
    return redirect('/')

# Take Today Attendance
def take_today_attendance_view(request):
  today_date = timezone.now().date()
  today_attendance = Attendance.objects.filter(date=today_date)
  all_employees = Employee.objects.all()
  if request.method == 'POST':
    for emp_attendance in today_attendance:
      is_present = request.POST.get(str(emp_attendance.employee.id))
      print(is_present)
      if is_present == 'on':
        emp_attendance.is_present = True
      else:
        emp_attendance.is_present = False
      emp_attendance.save()
    messages.info(request, f'Attendance Successfully updated')
    return redirect('/today_attendance/')  # Redirect to a success page after updating attendance

  context = {
      'all_employees': all_employees,
      'today_attendance': today_attendance
  }
  return render(request, 'take_attendance.html', context)

# Today Attendance list
def today_attendance_view(request):
  today_date = timezone.now().date()
  today_attendance = Attendance.objects.filter(date=today_date)
  all_employees = Employee.objects.all()
  for employee in all_employees:
    # Check if an attendance record exists for this employee and date
    attendance_exists = Attendance.objects.filter(employee=employee, date=today_date).exists()
    if not attendance_exists:
      # Attendance record does not exist, create a new one
      Attendance.objects.create(employee=employee, date=today_date, is_present=False)
      return redirect('/take_attendance/')
  context = {
    'today_attendance': today_attendance,
  }
  return render(request, 'today_attendance.html', context)

# All Attendance History
def all_attendance_view(request):
  all_attendance = Attendance.objects.all()
  context = {
    'all_attendance': all_attendance,
  }
  return render(request, 'all_attendance.html', context)