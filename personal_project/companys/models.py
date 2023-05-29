from django.db import models
from django.http import HttpRequest

from core.behaviors import (
    TimeStampedModel,
    AdressModel,
    CreatedByModel,
)
from personal_project.settings import AUTH_USER_MODEL


# Create your models here.

class Company(
    TimeStampedModel,
    AdressModel,
    # CreatedByModel,
    models.Model,
):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Company Name', max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField('Company Email', max_length=255, null=True, blank=True)
    phone = models.CharField('Company Phone', max_length=255, null=True, blank=True)
    website = models.CharField('Company Website', max_length=255, null=True, blank=True)
    document = models.CharField('Company Document', max_length=255, null=True, blank=True, unique=True)
    industry = models.CharField('Company Industry', max_length=255, null=True, blank=True)
    size = models.CharField('Company Size', max_length=255, null=True, blank=True)
    root = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='company', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def set_root(self, request: HttpRequest) -> None:
        if self.root is not None:
            raise Exception('Company root already been set')
        self.root = request.user
    
    
