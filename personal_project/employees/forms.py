from django import forms

from core.formsmixins import (
    RequestKwargFormMixin,
    PkRequestKwargsFormMixin,
)
from employees.models import EmployeeRoles, Employee
from core.utils import (
    get_current_user,
    get_current_employee,
    get_current_employee_company,
)



class CreateEmployeeRoleForm(
    RequestKwargFormMixin,
    forms.ModelForm
):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
            'description',
        ]
        
    def save(self, commit: bool = True) -> EmployeeRoles:
        role: EmployeeRoles = super().save(commit=False)
        role.set_company(
            company=get_current_employee_company(self.request)
        )
        role.set_created_by(
            employee=get_current_employee(self.request)
        )
        if commit:
            role.save()
        return role
        
        
        
class UpdateEmployeeRoleForm(
    PkRequestKwargsFormMixin,
    forms.ModelForm
):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
            'description',
        ]
    
    def save(self, commit: bool = True):
        role: EmployeeRoles =  super().save(commit=False)
        role.modified_by = get_current_user(self.request)
        if commit:
            role.save()
        return role        
        


class UpdateEmployeeForm(
    RequestKwargFormMixin,
    forms.ModelForm
):
    class Meta:
        model = Employee
        fields = [
            'work_email',
            'work_phone',
            'salary',
            'role',
            'is_active',
        ]
        