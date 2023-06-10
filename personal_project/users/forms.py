from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from allauth.account.models import EmailAddress
from django.db import transaction
from allauth.account.forms import ChangePasswordForm

from core.formsmixins import (
    RequestKwargFormMixin,
)
from core.utils import (
    set_fields_model_instance,
    update_instance_fields,
    get_current_user,
)
from users.models import User
from employees.models import Employee


from typing import Any, Dict



USER = get_user_model()


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
    group = forms.ChoiceField(choices=USER.Groups.choices, required=False)
    
    def save(self, request):
        user = super().save(request)
        try:
            set_fields_model_instance(
                instance=user, 
                cleaned_data=self.cleaned_data
            )
            Employee.objects.create(
                user=user,
            )
            user.save()
        except:
            user.delete()
            raise Exception("Error creating user.")
        return user



class UpdateUserEmailForm(
    RequestKwargFormMixin,
    forms.Form,
):
    email = forms.EmailField(required=True)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if self.request.user.email == email:
            raise forms.ValidationError(
                'The email was not changed.'
            )
        if EmailAddress.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Email already exists.'
            )
        return email

    
    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        if not self.request.user:
            raise forms.ValidationError(
                'No user'
            )
        return cleaned_data
    
    
    def save(self, commit: bool = True) -> Any:
        user = get_current_user(self.request)
        user.email = self.cleaned_data['email']
        with transaction.atomic():
            if commit:
                user.save()
                user.emailaddress_set.filter(
                    primary=1
                ).update(
                    email=self.cleaned_data['email']
                )
        return user



class UpdateUserPasswordForm(
    RequestKwargFormMixin,
    ChangePasswordForm,
):
    # oldpassword = PasswordField(
    #     label=_("Current Password"), autocomplete="current-password"
    # )
    # password1 = SetPasswordField(label=_("New Password"))
    # password2 = PasswordField(label=_("New Password (again)"))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.request.user
        return


class UpdateUserFieldsForm(
    RequestKwargFormMixin,
    forms.ModelForm
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = self.request.user
        return
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'document',
            'phone',
            'street',
            'number',
            'city',
            'state',
            'country',
            'birthday',
            'gender',
        ]
        
    
    def clean(self) -> Dict[str, Any]:
        cleaned_data =  super().clean()
        if not self.user == self.request.user:
            raise forms.ValidationError(
                'User does not match request user.'
            )
        return cleaned_data
    
        
    def save(self, commit: bool = True) -> Any:
        self.user = update_instance_fields(
            instance=self.user,
            data=self.cleaned_data
        )        
        if commit:
            self.user.save()
        return self.user
        
    
