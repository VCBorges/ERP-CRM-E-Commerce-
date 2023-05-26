from django.db import models
from django.contrib.auth import get_user_model



class AdministratorManager(models.Manager):

    
    def get_queryset(self, *args, **kwargs):
        from users.models import User
        result = super().get_queryset(*args, **kwargs)
        return result.filter(group=User.Groups.ADMINISTRATOR)
    
    


class MemberManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        from users.models import User
        result = super().get_queryset(*args, **kwargs)
        return result.filter(group=User.Groups.MEMBER)
    