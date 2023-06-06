from django import forms
from django.db import transaction

from core.formsmixins import RequestKwargFormMixin
from companys.models import Company
from users.utils import (
    current_user_is_root,
    current_employee_has_company,
    get_current_employee
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

        