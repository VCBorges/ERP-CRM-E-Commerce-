from django import forms
from django.db import transaction

from core.formsmixins import RequestKwargFormMixin
from companys.models import Company
from users.utils import (
    current_user_is_root,
    current_employee_has_company,
    get_current_employee,
    get_current_root_company,
)
from core.utils import (
    update_instance_fields,
)

from typing import Any, Dict



class CreateCompanyForm(
    RequestKwargFormMixin,
    forms.ModelForm
):
    class Meta:
        model = Company
        fields = [
            'name',
            'email',
            'phone',
            'website',
            'document',
            'industry',
            'size',
            'street',
            'number',
            'city',
            'state',
            'country',
            'postal_code'
        ]
        
    def clean(self) -> Dict[str, Any]:
        cleaned_data =  super().clean()
        if current_user_is_root(self.request):
            raise forms.ValidationError(
                "User already is company's root"
            )
        if current_employee_has_company(self.request):
            raise forms.ValidationError(
                'Employee already has a company'
            )
        return cleaned_data
        
    
    def save(self, commit: bool = True) -> Company:
        company: Company = super().save(commit=False)
        company.set_root(user=self.request.user)
        employee = get_current_employee(self.request)
        employee.set_company(company)
        if commit:
            with transaction.atomic():
                company.save()
                employee.save()
        return company




class UpdateCompanyForm(
    RequestKwargFormMixin,
    forms.ModelForm
):
    class Meta:
        model = Company
        fields = [
            'name',
            'email',
            'phone',
            'website',
            'industry',
            'size',
            'street',
            'number',
            'city',
            'state',
            'country',
            'postal_code'
        ]
        
    def clean(self) -> Dict[str, Any]:
        cleaned_data =  super().clean()
        if not current_user_is_root(self.request):
            raise forms.ValidationError(
                "User isn't company's root"
            )
        return cleaned_data
        
    
    def save(self, commit: bool = True) -> Any:
        company = get_current_root_company(self.request)
        company = update_instance_fields(
            instance=company,
            data=self.cleaned_data
        )        
        if commit:
            company.save()
        return company