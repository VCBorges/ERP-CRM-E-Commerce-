from django.urls import reverse

from companys.models import Company
from core.fixtures import auto_create_login_user, auto_create_company_login_user


import pytest




@pytest.mark.django_db
def test_create_company_view(auto_create_login_user):
    
    client,user = auto_create_login_user()

    form_data = {
        'name': 'unittest',
        'email': 'testcompany@test.com',
        'phone': '123456789',
        'website': 'unittest.com',
        'document': '123456789',
        'industry': 'unittest',
        'size': 'unittest',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'postal_code': '123456789',
    }
    
    response = client.post(
        reverse('company_create'),
        data=form_data
    )
    
    company = Company.objects.get(**form_data)
    employee = user.employee
    
    employee.refresh_from_db()
    
    assert response.status_code == 200
    assert company.name == form_data['name']
    assert company.email == form_data['email']
    assert company.phone == form_data['phone']
    assert company.website == form_data['website']
    assert company.document == form_data['document']
    assert company.industry == form_data['industry']
    assert company.size == form_data['size']
    assert company.street == form_data['street']
    assert company.number == form_data['number']
    assert company.city == form_data['city']
    assert company.state == form_data['state']
    assert company.country == form_data['country']
    assert company.postal_code == form_data['postal_code']
    assert company.root == user

    assert employee.company == company
    
    
    
@pytest.mark.django_db
def test_update_company_view(auto_create_company_login_user):
    
    client,user,company = auto_create_company_login_user()
    
    form_data = {
        'name': 'unittest2',
        'email': 'testecompany2@test.com',
        'phone': '123456781',
        'website': 'unittest2.com',
        'industry': 'unittest2',
        'size': 'unittest2',
        'street': 'unittest2',
        'number': '123',
        'city': 'unittest2',
        'state': 'unittest2',
        'country': 'unittest2',
        'postal_code': '123456782',
    }
    
    response = client.post(
        reverse('company_update'),
        data=form_data
    )
    company.refresh_from_db()
    
    assert response.status_code == 200
    assert company.name == form_data['name']
    assert company.email == form_data['email']
    assert company.phone == form_data['phone']
    assert company.website == form_data['website']
    assert company.industry == form_data['industry']
    assert company.size == form_data['size']
    assert company.street == form_data['street']
    assert company.number == form_data['number']
    assert company.city == form_data['city']
    assert company.state == form_data['state']
    assert company.country == form_data['country']
    assert company.postal_code == form_data['postal_code']
    assert company.root == user
    