from django.db import models

class TimeStampedModel(models.Model):

    '''
    Abstract base class model that provides self-updating
    '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
        
# class StatusModel(models.Model):

#     '''
#     Abstract base class model that provides status
#     '''
    
#     status = None
#     STATUS_CHOICES = None
#     status_verbose_name = 'Status'

#     status = models.CharField(verbose_name=status_verbose_name, default=default_status, max_length=30, choices=STATUS_CHOICES, blank=True, null=True)

#     class Meta:
#         abstract = True
        
