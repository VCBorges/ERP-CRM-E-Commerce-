from django.db import models

# from employees.models import Employee

class TimeStampedModel(models.Model):

    '''
    Abstract base class model that provides self-updating
    '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
        
class AdressModel:

    """
    Abstract base class model that provides address
    """
    
    street = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class CreatedByModel:

    """
    Abstract base class model that provides created by
    """

    created_by = models.OneToOneField('employees.Employee', on_delete=models.CASCADE, related_name='created_by', null=True, blank=True)

    class Meta:
        abstract = True