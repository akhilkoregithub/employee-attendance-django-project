from django.urls import path
from .views import (add_employee_view, update_employee_view, delete_employee_view, take_today_attendance_view,today_attendance_view,all_attendance_view)

urlpatterns = [

    path('', add_employee_view, name='employee'),
    path('update/<int:id>/', update_employee_view, name='update'),
    path('delete/<int:id>/', delete_employee_view, name='delete'),

    path('take_attendance/', take_today_attendance_view, name='take_attendance'),
    path('today_attendance/', today_attendance_view, name='today_attendance'),
    path('all_attendance/', all_attendance_view, name='all_attendance'),




]
