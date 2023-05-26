from django import forms

from core.formsmixins import RequestFormMixin
from employees.models import EmployeeRoles
from users.utils import (
    get_root_user_company_from_request,
    get_user_from_request,
)
        
        

class CreateEmployeeRoleForm(RequestFormMixin, forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
            'description',
        ]
        
        
    def save(self, commit: bool = True) -> EmployeeRoles:
        role: EmployeeRoles = super().save(commit=False)
        role.set_company(self.request)
        role.set_created_by(self.request)
        if commit:
            role.save()
        return role
        
        
        
class UpdateEmployeeRoleForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
        ]