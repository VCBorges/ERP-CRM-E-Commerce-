from django.http import JsonResponse
# from django.http import HttpResponseBadRequest, HttpResponseServerError
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


    @staticmethod
    def get_response(
        # self,
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


    @staticmethod
    def status_code_response(status_code: int) -> dict[str, int]:
        response = {'status': status_code}
        return response
    
    
    
    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        self.request = request
        form = self.form_instantiation(request)
        # print(form)
        try:
            if form.is_valid():
                print(form.cleaned_data)
                response = self.valid_form_response(form)
                status = self.status_code_response(200)
            else:
                print(form.errors)
                response = self.invalid_form_response(form)
                status = self.status_code_response(400)
        except Exception as e:
            print(e)
            traceback.print_exc()
            
            response = self.server_error_response()
            status = self.status_code_response(500)
        finally:
            return JsonResponse(response, **status)