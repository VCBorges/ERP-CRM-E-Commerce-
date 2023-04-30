from django.http import JsonResponse
from django.forms import ModelForm
from django.forms import Form
from django.http import QueryDict

from core.utils import get_form_errors


import traceback



class RegularTemplateViewMixin:
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class RegularModelFormSubmissionViewMixin:
    
    form_class: ModelForm = None
    valid_form_message: str = None
    invalid_form_message: str = None
    server_error_message: str = 'There was an error processing your request. Please try again later.'

    def get_response(
        self,
        status: int,
        message:str, 
        errors=None, 
        *args, 
        **kwargs
    ) -> dict:
        
        response = {
            'status': status,
            'message': message,
        }
        
        if errors:
            response['errors'] = errors
        
        return response
    
    
    def form_methods(self, form: ModelForm, *args, **kwargs) -> bool:
        form.save()
        return True
    
    
    
    def form_instantiation(self, request: QueryDict, *args, **kwargs) -> ModelForm | Form:
        form: ModelForm = self.form_class(
            request.POST,
            request=request
        )

        return form
    
        

    def valid_form_response(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if form.is_valid():

            self.form_methods(form)
            
            response = self.get_response(
                status=200,
                message=self.valid_form_message,
            )
            return response
     

        
    def invalid_form_response(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if not form.is_valid():
            errors = get_form_errors(form)

            response = self.get_response(
                status=400,
                message=self.invalid_form_message,
                errors=errors
            )
            return response
        
    
    
    def server_error_response(self, *args, **kwargs) -> dict:
        response = {
            'status': 500,
            'message': self.server_error_message
        }
        return response
        
    
    
    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        self.request = request
        form = self.form_instantiation(request)
            
        try:
            if form.is_valid():
                response = self.valid_form_response(form)
            else:
                response = self.invalid_form_response(form)
        except Exception as e:
            print(e)
            
            traceback.print_exc()
            
            response = self.server_error_response()
        finally:
            return JsonResponse(response)