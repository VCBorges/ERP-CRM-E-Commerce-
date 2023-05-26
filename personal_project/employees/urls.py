from django.urls import path, include
from employees.views import EmployeeTemplateView
from employees.views import CreateEmployeeRoleView

urlpatterns = [
    path('', EmployeeTemplateView.as_view(), name='employees'),
    path('create/', CreateEmployeeRoleView.as_view(), name='create_employee_role'),
]
