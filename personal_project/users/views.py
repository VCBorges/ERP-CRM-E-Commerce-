from typing import Any
from django import http
from django.forms import Form, ModelForm
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django.contrib.auth.views import LogoutView

# from core.viewmixins import RegularTemplateViewMixin
from core.views import ModelFormSubmissionView, BaseTemplateView
from users.forms import CreateUserForm



class UserRegistrationView(ModelFormSubmissionView):
    
    form_class = CreateUserForm
    valid_form_message = 'User created successfully.'
    invalid_form_message = 'There was an error creating the user. Please try again later.'
    
    
    @method_decorator(csrf_exempt)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    
    def form_instantiation(self, request: QueryDict, *args, **kwargs) -> ModelForm | Form:
        form = self.form_class(
            request.POST,
        )
        return form
    
    
    def form_methods(self, form: ModelForm, *args, **kwargs) -> bool:
        form.save(
            self.request
        )
        return True
    
    
    
    
class UserLoginView(ModelFormSubmissionView):
    
    form_class = LoginForm
    valid_form_message = 'User logged in successfully.'
    invalid_form_message = 'There was an error logging in the user. Please try again later.'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    
    def form_methods(self, form: LoginForm, *args, **kwargs) -> bool:
        form.login(
            self.request,
        )
        return True
    



class UserLogoutView(LogoutView):
    pass



class LoginTemplateView(BaseTemplateView):
    
    template_name = 'users/login.html'
    
    def get(self, request, *args, **kwargs):
        print(request.user.company)
        return super().get(request, *args, **kwargs)
    
    