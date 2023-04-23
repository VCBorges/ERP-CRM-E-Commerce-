from django.urls import path, include
from employees.views import EmployeeTemplateView
from employees.views import CreateEmployeeView
from employees.views import CreateEmployeeRoleView

urlpatterns = [
    path('', EmployeeTemplateView.as_view(), name='employees'),
    path('create/', CreateEmployeeView.as_view(), name='create_employee'),
    path('create-role/', CreateEmployeeRoleView.as_view(), name='create_employee_role'),
]
