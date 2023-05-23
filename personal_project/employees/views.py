from django.http import JsonResponse, QueryDict
from django.views.generic import View, UpdateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from core.viewmixins import RegularModelFormSubmissionViewMixin
from core.viewmixins import RegularTemplateViewMixin
from core.views import ModelFormSubmissionView, CreateRequestModelFormView
from employees.forms import CreateEmployeeRoleForm


class EmployeeTemplateView(RegularTemplateViewMixin, TemplateView):
    
    template_name = 'employees/employees.html'
    
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
    

    
    
    
class CreateEmployeeRoleView(CreateRequestModelFormView):
    
    form_class = CreateEmployeeRoleForm
    valid_form_message = 'Employee role created successfully.'
    invalid_form_message = 'There was an error creating the employee role. Please try again later.'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        return super().post(request, *args, **kwargs)
    
    
    