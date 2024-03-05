from django.contrib import admin
from .models import Employee, Attendance

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("department", "mobile", "email", "name", "ch")


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("is_present", "date", "employee")
