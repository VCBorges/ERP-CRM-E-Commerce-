# from django.views.generic import View, UpdateView
# from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

# from core.viewmixins import RegularModelFormSubmissionViewMixin
# from core.viewmixins import RegularTemplateViewMixin
# from companys.forms import CreateCompanyForm
# from core.views import ModelFormSubmissionView, BaseTemplateView, CreateRequestModelFormView



# class CompanyTemplateView(RegularTemplateViewMixin, TemplateView):
    
#     template_name = 'companys/companys.html'
    
    
# class CompanyCreateView(CreateRequestModelFormView):
    
#     form_class = CreateCompanyForm
#     valid_form_message = 'Company created successfully.'
#     invalid_form_message = 'There was an error creating the company. Please try again later.'
    
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)