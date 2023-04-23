from django.db import models

from core.behaviors import TimeStampedModel
from core.behaviors import StatusModel
from companys.models import Company

# Create your models here.

class Customer(TimeStampedModel, StatusModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Customer Name', max_length=255, unique=True, null=True, blank=True)
    document = models.CharField('Customer Document', max_length=255, null=True, blank=True)
    email = models.EmailField('Customer Email', max_length=255, null=True, blank=True)
    phone = models.CharField('Customer Phone', max_length=255, null=True, blank=True)
    address = models.CharField('Customer Address', max_length=255, null=True, blank=True)
    website = models.CharField('Customer Website', max_length=255, null=True, blank=True)
    document = models.CharField('Customer Document', max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='customers', null=True, blank=True)
    company_name = models.CharField('Company Name', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name