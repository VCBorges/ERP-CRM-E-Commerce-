from django.db import models



class TimeStampedModel(models.Model):
    """
    Abstract base class model that provides self-updating
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        
        
        
class AdressModel(models.Model):
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



class CreatedByModel(models.Model):
    """
    Abstract base class model that provides created by
    """
    created_by = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='%(class)s_created', null=True, blank=True)
    modified_by = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='%(class)s_modified', null=True, blank=True)

    class Meta:
        abstract = True
        
    def get_model_verbose_name(self):
        return self._meta.verbose_name1
    
    