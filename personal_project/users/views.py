from django.forms import Form, ModelForm
from django.http import QueryDict
from allauth.account.forms import LoginForm
from django.contrib.auth.views import LogoutView

from core.views import (
    BaseTemplateView,
    BaseFormView,
)
from users.forms import CreateUserForm



class UserRegistrationView(BaseFormView):
    
    form_class = CreateUserForm
    form_valid_message = 'User created successfully.'
    form_invalid_message = 'There was an error creating the user. Please try again later.'
    
    
    def form_methods(self, form: ModelForm, *args, **kwargs) -> bool:
        form.save(
            request=self.request,
        )
        return True
    
    
    
class UserLoginView(BaseFormView):
    
    form_class = LoginForm
    form_valid_message = 'User logged in successfully.'
    form_invalid_message = 'There was an error logging in the user. Please try again later.'
    
    def form_methods(self, form: LoginForm, *args, **kwargs) -> bool:
        form.login(
            request=self.request,
        )
        return True
    



class UserLogoutView(LogoutView):
    pass



class LoginTemplateView(BaseTemplateView):
    
    template_name = 'users/login.html'
    
    def get(self, request, *args, **kwargs):
        print(request.user.company)
        return super().get(request, *args, **kwargs)
    
    