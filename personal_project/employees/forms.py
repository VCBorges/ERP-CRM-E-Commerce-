from django import forms

from employees.models import Employee
from employees.models import EmployeeRoles


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
        ]
        
        
        
class UpdateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
        ]
        
        

class CreateEmployeeRoleForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
            'description',
        ]
        
        
        
class UpdateEmployeeRoleForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoles
        fields = [
            'name',
        ]