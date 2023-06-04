from django.views.generic import View, UpdateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.forms import CreateCompanyForm

from core.views import (
    BaseTemplateView,
    BaseFormView,
    BaseRequestFormView,
)



# class CompanyTemplateView(RegularTemplateViewMixin, TemplateView):
    
#     template_name = 'companys/companys.html'
    
    
class CompanyCreateView(BaseRequestFormView):
    
    form_class = CreateCompanyForm
    valid_form_message = 'Company created successfully.'
    invalid_form_message = 'There was an error creating the company. Please try again later.'
    