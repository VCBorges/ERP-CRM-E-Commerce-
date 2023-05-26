from django.db import models
from django.http import HttpRequest

from core.behaviors import TimeStampedModel
from personal_project.settings import AUTH_USER_MODEL


# Create your models here.

class Company(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Company Name', max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField('Company Email', max_length=255, null=True, blank=True)
    phone = models.CharField('Company Phone', max_length=255, null=True, blank=True)
    website = models.CharField('Company Website', max_length=255, null=True, blank=True)
    document = models.CharField('Company Document', max_length=255, null=True, blank=True)
    industry = models.CharField('Company Industry', max_length=255, null=True, blank=True)
    size = models.CharField('Company Size', max_length=255, null=True, blank=True)
    street = models.CharField('User Street', max_length=255, null=True, blank=True)
    number = models.CharField('User Number', max_length=255, null=True, blank=True)
    city = models.CharField('User City', max_length=255, null=True, blank=True)
    state = models.CharField('User State', max_length=255, null=True, blank=True)
    country = models.CharField('User Country', max_length=255, null=True, blank=True)
    postal_code = models.CharField('User Postal Code', max_length=255, null=True, blank=True)
    root = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def set_root(self, request: HttpRequest) -> None:
        if self.root is not None:
            raise Exception('Company root already been set')
        self.root = request.user
    
    
