from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    ch = (('Development', 'Development'), ('Testing', 'Testing'),('HR', 'HR'),)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    department = models.CharField(max_length=200, choices=ch)

    def __str__(self):
        return f"{self.name} - {self.department}"
    
    @property
    def today_attendance(self):
        return Attendance.objects.filter(employee=self,date=timezone.now().date(),is_present=True).first()

    

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.date}"