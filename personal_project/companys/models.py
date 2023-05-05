from django.db import models
from core.behaviors import TimeStampedModel
from core.behaviors import StatusModel

# Create your models here.

class Company(TimeStampedModel, StatusModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Company Name', max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField('Company Email', max_length=255, null=True, blank=True)
    phone = models.CharField('Company Phone', max_length=255, null=True, blank=True)
    address = models.CharField('Company Address', max_length=255, null=True, blank=True)
    website = models.CharField('Company Website', max_length=255, null=True, blank=True)
    document = models.CharField('Company Document', max_length=255, null=True, blank=True)
    Industry = models.CharField('Company Industry', max_length=255, null=True, blank=True)
    size = models.CharField('Company Size', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    
# class CompanyIn