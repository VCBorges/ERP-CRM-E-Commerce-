from django.http import JsonResponse, QueryDict
from django.views.generic import View, UpdateView
from django.views.generic import TemplateView

from core.views import (
    BaseTemplateView,
    BaseRequestFormView,
)
from employees.forms import (
    CreateEmployeeRoleForm,
    UpdateEmployeeRoleForm,
    UpdateEmployeeForm
    
)



class UpdateEmployeeView(BaseRequestFormView):
    form_class = UpdateEmployeeForm
    form_valid_message = 'Employee updated successfully.'
    form_invalid_message = 'There was an error updating the employee. Please try again later.'



class UpdateEmployeeRoleView(BaseRequestFormView):
    form_class = UpdateEmployeeRoleForm
    form_valid_message = 'Employee role updated successfully.'
    form_invalid_message = 'There was an error updating the employee role. Please try again later.'
    
    
    
class CreateEmployeeRoleView(BaseRequestFormView):
    form_class = CreateEmployeeRoleForm
    form_valid_message = 'Employee role created successfully.'
    form_invalid_message = 'There was an error creating the employee role. Please try again later.'
