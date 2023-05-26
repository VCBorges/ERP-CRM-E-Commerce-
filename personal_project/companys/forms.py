from django import forms
from django.db import transaction

from core.formsmixins import RequestFormMixin
from companys.models import Company
from users.utils import (
    set_employee_company,
    user_is_root,
    employee_has_company,
)


from typing import Any, Dict



class CreateCompanyForm(
    RequestFormMixin,
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
        if user_is_root(self.request):
            raise forms.ValidationError(
                'User already is company root'
            )
        if employee_has_company(self.request):
            raise forms.ValidationError(
                'Employee already has a company'
            )
        return cleaned_data
        
        
    
    def save(self, commit: bool = True) -> Company:
        company: Company = super().save(commit=False)
        company.set_root(self.request.user)
        employee = set_employee_company(
            request=self.request,
            company=company
        )
        if commit:
            with transaction.atomic():
                company.save()
                employee.save()
        return company

        