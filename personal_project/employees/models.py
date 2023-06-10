from django.db import models

from personal_project.settings import AUTH_USER_MODEL
from core.behaviors import (
    TimeStampedModel,
    CreatedByModel,
)
# from users.models import User
from companys.models import Company
from employees.managers import EmployeeManager
from core.utils import (
    get_current_employee_company,
)



class EmployeeRoles(
    TimeStampedModel,
    CreatedByModel,
    models.Model,
):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Role Name', max_length=255, unique=True, null=True, blank=True)
    description = models.TextField('Role Description', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='roles', null=True, blank=True)
    department = models.ForeignKey('human_resources.Department', on_delete=models.CASCADE, related_name='roles', null=True, blank=True)

    
    def __str__(self):
        return self.name + ' - ' + self.company.name
    
    
    def set_company(self, company: Company) -> None:
        if self.company is not None:
            raise Exception('Employee role already has a company')
        self.company = company
        
        
    def set_created_by(self, employee) -> None:
        if self.created_by is not None:
            raise Exception('Employee role already has a creator')
        self.created_by = employee
    
        

class Employee(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    work_phone = models.CharField('Employee Phone', max_length=255, null=True, blank=True)
    work_email = models.EmailField('Employee Email', max_length=255, null=True, blank=True)
    hire_date = models.DateField('Employee Hire Date', null=True, blank=True)
    salary = models.DecimalField('Employee Salary', max_digits=10, decimal_places=2, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    role = models.ForeignKey(EmployeeRoles, on_delete=models.CASCADE, related_name='employee', null=True, blank=True)
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee', null=True, blank=True)
    is_active = models.BooleanField('Employee is Active', default=True)

    objects = EmployeeManager()

    def __str__(self):
        return self.user.get_full_name() + ' - ' + self.company.name
    
    def set_company(self, company: Company) -> None:
        if self.company is not None:
            raise Exception('Employee already has a company')
        self.company = company
    
    
