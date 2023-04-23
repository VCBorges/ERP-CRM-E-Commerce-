from django.http import JsonResponse
from django.forms import ModelForm
from django.forms import Form
from django.http import QueryDict

from core.utils import get_form_errors


class RegularTemplateViewMixin:
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class RegularModelFormSubmissionViewMixin:
    
    form_class: ModelForm = None
    form_valid_message: str = None
    form_invalid_message: str = None
    server_error_message: str = 'There was an error processing your request. Please try again later.'

    def form_methods_mixin(self, methods: list[str]):
        pass

    def form_valid_mixin(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if form.is_valid():
            form.save()
            response = {
                'status': 200,
                'message': self.form_valid_message
            }
            return response
     
     
        
    def form_invalid_mixin(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if not form.is_valid():
            errors = get_form_errors(form)
            response = {
                'status': 400,
                'message': self.form_invalid_message,
                'errors': errors
            }
            return response
        
    
    
    def form_server_error_mixin(self, *args, **kwargs) -> dict:
        response = {
            'status': 500,
            'message': self.server_error_message
        }
        return response
        
    
    
    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        form: ModelForm = self.form_class(request.POST, request=request)
        try:
            if form.is_valid():
                response = self.form_valid_mixin(form)
            else:
                response = self.form_invalid_mixin(form)
        except Exception as e:
            response = self.form_server_error_mixin()
        finally:
            return JsonResponse(response)