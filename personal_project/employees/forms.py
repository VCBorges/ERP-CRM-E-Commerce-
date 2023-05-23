from django import forms

from core.formsmixins import RequestFormMixin
from employees.models import EmployeeRoles
from users.utils import (
    get_user_company_from_request,
)


        
        
        

class CreateEmployeeRoleForm(RequestFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
            'description',
        ]
        
        
    def save(self, commit: bool = True):
        role = super().save(commit=False)
        role.company = get_user_company_from_request(self.request)
        if commit:
            role.save()
        return role
        
        
        
class UpdateEmployeeRoleForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
        ]