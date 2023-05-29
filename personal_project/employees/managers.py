from django.db import models
from typing import ForwardRef



class EmployeeManager(models.Manager):

    def create(self, user):
        from employees.models import Employee
        employee = Employee(
            user=user,
            work_phone=user.phone,
            work_email=user.email,
        )
        return employee