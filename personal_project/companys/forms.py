from django import forms
from django.db import transaction


from core.formsmixins import RequestFormMixin
from companys.models import Company
from users.utils import (
    set_employees_company,
    user_has_company,
    get_user_from_request,
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
        if user_has_company(self.request):
            raise forms.ValidationError(
                'User already has a company'
            )
        return cleaned_data
        
        
    
    def save(self, commit: bool = True) -> Company:
        company: Company = super().save(commit=False)
        company.root = get_user_from_request(self.request)
        employee = set_employees_company(
            self.request,
            company
        )
        if commit:
            with transaction.atomic():
                company.save()
                employee.save()
        return company

        