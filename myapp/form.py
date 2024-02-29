from django import forms
from .models import Employee, Attendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'mobile': 'Mobile',
            'department': 'Department',

        }
        error_messages = {
        'name':{'required':'Name is required!'},
        'email':{'required':'Email is required!'},
        'mobile': {'required':'Mobile is required!'},
        'department': {'required': 'Please select department!'},
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            # 'is_present': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }

