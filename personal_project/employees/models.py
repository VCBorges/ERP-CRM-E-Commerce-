from django.db import models

from core.behaviors import TimeStampedModel
from core.behaviors import StatusModel
from companys.models import Company



class EmployeeRoles(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Role Name', max_length=255, unique=True, null=True, blank=True)
    description = models.TextField('Role Description', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='roles', null=True, blank=True)
    company_name = models.CharField('Company Name', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name



class Employee(TimeStampedModel, StatusModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Employee Name', max_length=255, null=True, blank=True)
    document = models.CharField('Employee Document', max_length=255, null=True, blank=True)
    email = models.EmailField('Employee Email', max_length=255, null=True, blank=True)
    phone = models.CharField('Employee Phone', max_length=255, null=True, blank=True)
    address = models.CharField('Employee Address', max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    company_name = models.CharField('Company Name', max_length=255, null=True, blank=True)
    role = models.ForeignKey(EmployeeRoles, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    role_name = models.CharField('Role Name', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name