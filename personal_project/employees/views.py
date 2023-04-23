from django.views.generic import View, UpdateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.viewmixins import RegularModelFormSubmissionViewMixin
from core.viewmixins import RegularTemplateViewMixin
from employees.forms import CreateEmployeeForm
from employees.forms import CreateEmployeeRoleForm


class EmployeeTemplateView(RegularTemplateViewMixin, TemplateView):
    
    template_name = 'employees/employees.html'
    
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    

class CreateEmployeeView(RegularModelFormSubmissionViewMixin, View):
    
    form_class = CreateEmployeeForm
    form_valid_message = 'Employee created successfully.'
    form_invalid_message = 'There was an error creating the employee. Please try again later.'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    
class CreateEmployeeRoleView(RegularModelFormSubmissionViewMixin, View):
    
    form_class = CreateEmployeeRoleForm
    form_valid_message = 'Employee role created successfully.'
    form_invalid_message = 'There was an error creating the employee role. Please try again later.'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)