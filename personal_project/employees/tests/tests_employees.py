from django.urls import reverse

from employees.models import Employee, EmployeeRoles
from core.fixtures import (
    auto_create_login_user,
    auto_create_company_login_user,
    auto_create_employee_role,
)


import pytest


@pytest.mark.django_db
def test_create_employee_role_view(auto_create_company_login_user):
    
    client,user,company = auto_create_company_login_user()

    form_data = {
        'name': 'unittest',
        'description': 'unittest',
    }
    
    response = client.post(
        reverse('create_employee_role'),
        data=form_data
    )
    
    employee_role = EmployeeRoles.objects.get(**form_data)
     
    assert response.status_code == 200
    assert employee_role.name == form_data['name']
    assert employee_role.description == form_data['description']
    assert employee_role.company == company
    assert employee_role.created_by == user.employee