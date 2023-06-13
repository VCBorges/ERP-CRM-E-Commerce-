from django.http import JsonResponse, QueryDict
from django.views.generic import View, UpdateView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.forms import (
    CreateCompanyForm,
    UpdateCompanyForm,
)

from core.views import (
    BaseTemplateView,
    BaseFormView,
    BaseRequestFormView,
)



# class CompanyTemplateView(RegularTemplateViewMixin, TemplateView):
    
#     template_name = 'companys/companys.html'
    
    
class CompanyCreateView(BaseRequestFormView):
    
    form_class = CreateCompanyForm
    form_valid_message = 'Company created successfully.'
    form_invalid_message = 'There was an error creating the company. Please try again later.'

    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        # print(f'User: {request.user}')
        return super().post(request, *args, **kwargs)


class UpdateCompanyView(BaseRequestFormView):
    
    form_class = UpdateCompanyForm
    form_valid_message = 'Company updated successfully.'
    form_invalid_message = 'There was an error updating the company. Please try again later.'