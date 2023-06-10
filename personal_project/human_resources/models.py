from django.db import models

from core.behaviors import (
    TimeStampedModel,
    AdressModel,
    CreatedByModel,
)
# Create your models here.


class Department(
    TimeStampedModel,
    AdressModel,
    CreatedByModel,
    models.Model
):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField('Department Name', max_length=255, unique=True, null=True, blank=True)
    description = models.TextField('Department Description', null=True, blank=True)
    company = models.ForeignKey('companys.Company', on_delete=models.CASCADE, related_name='departments', null=True, blank=True)
    
    def __str__(self):
        return self.name