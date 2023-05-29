from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms import formset_factory
# from django.http import HttpResponseBadRequest, HttpResponseServerError

from django.forms import ModelForm
from django.forms import Form
from django.http import QueryDict
from django.views.generic import UpdateView

from core.utils import get_form_errors


import traceback



class BaseContextTemplateViewMixin:
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    


class BaseFormViewMixin:
    
    form_class: ModelForm = None
    form_valid_message: str = None
    form_invalid_message: str = None
    server_error_message: str = 'There was an error processing your request. Please try again later.'

    @staticmethod
    def get_response(
        status: int,
        message:str, 
        additional_data: dict = None,
        *args, 
        **kwargs
    ) -> dict:
        response = {
            'status': status,
            'message': message,
        }
        if additional_data:
            response.update(additional_data)
        return response
    
    
    def form_methods(self, form: ModelForm, *args, **kwargs) -> None:
        return 
    
    
    def get_form(self, *args, **kwargs) -> ModelForm | Form:
        form: ModelForm = self.form_class(
            **self.get_form_kwargs()
        )
        return form

    
    def get_form_kwargs(self, *args, **kwargs) -> dict:
        kwargs['data'] = self.request.POST
        return kwargs
        

    def form_valid(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if form.is_valid():
            self.form_methods(form)
            response = self.get_response(
                status=200,
                message=self.form_valid_message,
            )
            return response
     
        
    def form_invalid(self, form: ModelForm | Form, *args, **kwargs) -> dict:
        if not form.is_valid():
            errors = get_form_errors(form)
            response = self.get_response(
                status=400,
                message=self.form_invalid_message,
                additional_data=errors
            )
            return response
        
    
    def server_error(self, exception, *args, **kwargs) -> dict:
        response = self.get_response(
            status=500,
            message=self.server_error_message,
            additional_data=exception,
        )
        return response


    @staticmethod
    def status_code_response(status_code: int) -> dict[str, int]:
        response = {'status': status_code}
        return response
    
    
    def post(self, request: QueryDict, *args, **kwargs) -> JsonResponse:
        self.request = request
        form = self.get_form()
        try:
            if form.is_valid():
                print(form.cleaned_data)
                response = self.form_valid(form)
                status = self.status_code_response(200)
            else:
                print(form.errors)
                response = self.form_invalid(form)
                status = self.status_code_response(400)
        except Exception as e:
            traceback.print_exc()
            
            response = self.server_error(
                exception={
                    'error': str(e)
                    }
            )
            status = self.status_code_response(500)
        finally:
            return JsonResponse(response, **status)
        
    

class RequestFormKwargsMixin:
    def get_form_kwargs(self, *args, **kwargs) -> dict:
        kwargs['data'] = self.request.POST
        kwargs['request'] = self.request
        return kwargs
    
    
    
class RequestFilesFormKwargsMixin:
    def get_form_kwargs(self, *args, **kwargs) -> dict:
        kwargs['data'] = self.request.POST
        kwargs['files'] = self.request.FILES
        kwargs['request'] = self.request
        return kwargs    
    
    
    
class BaseUpdateFormViewMixin:
    
    def get_form_kwargs(self, *args, **kwargs) -> dict:
        kwargs['data'] = self.request.POST
        kwargs['pk'] = self.pk
        return kwargs
    
    
    def post(self, request: QueryDict, pk, *args, **kwargs):
        self.pk = pk
        return super().post(request, pk, *args, **kwargs)
    
    
    
class ModelFormMethodsMixin:
    def form_methods(self, form: ModelForm, *args, **kwargs) -> bool:
        form.save()
        return True



class UpdateResquestFormKwargsMixin:
    def get_form_kwargs(self, *args, **kwargs) -> dict:
        kwargs = super().get_form_kwargs()    
        kwargs['request'] = self.request
        return kwargs

    

class CsrfExemptMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)