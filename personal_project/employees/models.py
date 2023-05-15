from django.db import models
from django.contrib.auth import get_user_model

from personal_project.settings import AUTH_USER_MODEL
from core.behaviors import TimeStampedModel
from core.behaviors import StatusModel
from companys.models import Company

user = get_user_model()

class EmployeeRoles(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Role Name', max_length=255, unique=True, null=True, blank=True)
    description = models.TextField('Role Description', null=True, blank=True)
    company_name = models.CharField('Company Name', max_length=255, null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    



class Employee(TimeStampedModel, StatusModel):
    id = models.AutoField(primary_key=True)
    work_phone = models.CharField('Employee Phone', max_length=255, null=True, blank=True)
    work_email = models.CharField('Employee Email', max_length=255, null=True, blank=True)
    hire_date = models.DateField('Employee Hire Date', null=True, blank=True)
    salary = models.DecimalField('Employee Salary', max_digits=10, decimal_places=2, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    role = models.ForeignKey(EmployeeRoles, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='employee', null=True, blank=True)

    def __str__(self):
        return self.user.username, self.company.name, self.role.name