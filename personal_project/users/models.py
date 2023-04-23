from django.contrib.auth.models import AbstractUser
from django.db import models

from companys.models import Company
from employees.models import Employee, EmployeeRoles
# from companys.models import Employee
# from companys.models import EmployeeRoles

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    company_name = models.CharField('Company Name', max_length=255, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    role = models.ForeignKey(EmployeeRoles, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    pass