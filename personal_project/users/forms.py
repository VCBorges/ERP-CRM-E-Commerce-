from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

from core.utils import set_fields_model_instance
from personal_project.settings import AUTH_USER_MODEL
from employees.models import EmployeeRoles, Employee




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
        cleaned_data = self.cleaned_data
        set_fields_model_instance(
            instance=user, 
            cleaned_data=cleaned_data
        )
        employee = Employee(
            work_phone=user.phone,
            work_email=user.email,
            user=user
        )
        user.save()
        employee.save()
        return user