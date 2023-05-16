from django.db import models

from personal_project.settings import AUTH_USER_MODEL



class AdministratorManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(group=AUTH_USER_MODEL.Groups.ADMINISTRATOR)
    
    


class MemberManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(group=AUTH_USER_MODEL.Groups.MEMBER)
    