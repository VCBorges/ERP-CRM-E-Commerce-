from django.forms import ModelForm
from allauth.account.forms import LoginForm
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse, QueryDict

from core.views import (
    BaseTemplateView,
    BaseFormView,
    BaseRequestFormView,
)
from users.forms import (
    CreateUserForm,
    UpdateUserEmailForm,
    UpdateUserPasswordForm,
    UpdateUserFieldsForm,
)



class UserRegistrationView(BaseFormView):
    
    form_class = CreateUserForm
    form_valid_message = 'User created successfully.'
    form_invalid_message = 'There was an error creating the user. Please try again later.'
    
    
    def form_methods(self, form: ModelForm, *args, **kwargs) -> bool:
        form.save(
            request=self.request,
        )
        return True
    
    
    
class UserLoginView(BaseRequestFormView):
    
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



class UpdateUserEmailView(BaseRequestFormView):
    
    form_class = UpdateUserEmailForm
    form_valid_message = 'User email updated successfully.'
    form_invalid_message = 'There was an error updating the user email. Please try again later.'
    
    
class UpdateUserPasswordView(BaseRequestFormView):
    
    form_class = UpdateUserPasswordForm
    form_valid_message = 'User password updated successfully.'
    form_invalid_message = 'There was an error updating the user password. Please try again later.'
    
    
    
class UpdateUserFieldsView(BaseRequestFormView):
    
    form_class = UpdateUserFieldsForm
    form_valid_message = 'User fields updated successfully.'
    form_invalid_message = 'There was an error updating the user fields. Please try again later.'


class LoginTemplateView(BaseTemplateView):
    
    template_name = 'users/login.html'
    
    def get(self, request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)
    
    