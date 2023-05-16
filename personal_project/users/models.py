from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import AdministratorManager, MemberManager


import datetime


class User(AbstractUser):
    
    class Groups(models.TextChoices):
        ADMINISTRATOR = 'administrator', 'Administrator'
        MEMBER = 'member', 'Member'
    
    middle_name = models.CharField('User Middle Name', max_length=255, null=True, blank=True)
    document = models.CharField('User Document', max_length=255, null=True, blank=True)
    phone = models.CharField('User Phone', max_length=255, null=True, blank=True)
    street = models.CharField('User Street', max_length=255, null=True, blank=True)
    number = models.CharField('User Number', max_length=255, null=True, blank=True)
    city = models.CharField('User City', max_length=255, null=True, blank=True)
    state = models.CharField('User State', max_length=255, null=True, blank=True)
    country = models.CharField('User Country', max_length=255, null=True, blank=True)
    postal_code = models.CharField('User Postal Code', max_length=255, null=True, blank=True)
    gender = models.CharField('User Gender', max_length=255, null=True, blank=True)
    birthday = models.DateField('User Birthday', null=True, blank=True)
    group = models.CharField('User Group', max_length=255, null=True, blank=True, choices=Groups.choices, default=Groups.MEMBER)
    
    def get_full_name(self):
        return f'{self.first_name} {self.middle_name or ""} {self.last_name}'
    
    def get_age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
    
    
    
    
class Administrator(User):
    
    objects = AdministratorManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'
        
        


class Member(User):
    
    objects = MemberManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Member'
        verbose_name_plural = 'Members'