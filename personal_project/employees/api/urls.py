from django.urls import path

from employees.api import views

urlpatterns = [
    path('datatable/', views.EmployeeDataTableAPIView.as_view(), name='employees_datatable'),
]
