from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from core.utils import set_fields_model_instance



class CreateUserForm(SignupForm):

    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    document = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    street = forms.CharField(required=False)
    number = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    birthday = forms.DateField(required=False)
    gender = forms.CharField(required=False)
    
    
    def save(self, request):
        user = super().save(request)
        cleaned_data = self.cleaned_data
        set_fields_model_instance(
            instance=user, 
            cleaned_data=cleaned_data
        )
        user.save()
        return user