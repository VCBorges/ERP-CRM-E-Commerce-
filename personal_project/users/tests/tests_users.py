from django.urls import reverse
from django.test import RequestFactory

from users.models import User
from employees.models import Employee
from core.factories import (
    set_session_middleware,
    get_test_view_response,
)
from users import views


import json
import pytest
import datetime




@pytest.mark.django_db
def test_user_create_view(client):
    factory = RequestFactory()

    form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
        'first_name': 'unittest',
        'middle_name': 'unittest',
        'last_name': 'unittest',
        'document': '123456789',
        'phone': '123456789',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'gender': 'unittest',
        'birthday': '1990-01-01',
    }

    request = factory.post(reverse('register'), data=form_data)

    response = get_test_view_response(
        view=views.UserRegistrationView,
        request=request,
    )
    
    print(request)
    
    del form_data['password1']
    
    user = User.objects.get(**form_data)
    employee = Employee.objects.get(user=user)
    
    response_data = json.loads(response.content.decode('utf-8'))
    
    assert response.status_code == 200
    assert response_data['message'] == 'User created successfully.'
    assert user.email == form_data['email']
    assert user.first_name == form_data['first_name']
    assert user.middle_name == form_data['middle_name']
    assert user.last_name == form_data['last_name']
    assert user.document == form_data['document']
    assert user.phone == form_data['phone']
    assert user.street == form_data['street']
    assert user.number == form_data['number']
    assert user.city == form_data['city']
    assert user.state == form_data['state']
    assert user.country == form_data['country']
    assert user.gender == form_data['gender']
    assert user.birthday == datetime.date(1990, 1, 1)
    
    assert employee.work_email == user.email
    assert employee.work_phone == user.phone
    assert employee.user == user
    
    

@pytest.mark.django_db
def test_user_update_email_view(client):
    
    form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
        'first_name': 'unittest',
        'middle_name': 'unittest',
        'last_name': 'unittest',
        'document': '123456789',
        'phone': '123456789',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'gender': 'unittest',
        'birthday': '1990-01-01',
    }
    
    response = client.post(
        reverse('register'),
        data=form_data
    )
    
    del form_data['password1']
    
    user = User.objects.get(**form_data)
    
    response_data = json.loads(response.content.decode('utf-8'))
    
    assert response.status_code == 200
    assert response_data['message'] == 'User created successfully.'
    assert user.email == form_data['email']
    assert user.first_name == form_data['first_name']
    assert user.middle_name == form_data['middle_name']
    assert user.last_name == form_data['last_name']
    assert user.document == form_data['document']
    assert user.phone == form_data['phone']
    assert user.street == form_data['street']
    assert user.number == form_data['number']
    assert user.city == form_data['city']
    assert user.state == form_data['state']
    assert user.country == form_data['country']
    assert user.gender == form_data['gender']
    assert user.birthday == datetime.date(1990, 1, 1)
    
    client.force_login(user)
    
    assert user.is_authenticated

    form_data = {
        'email': 'unittest2@test.com',
    }
    
    response = client.post(
        reverse('update_user_email'),
        data=form_data
    )
    
    user.refresh_from_db()
    
    assert response.status_code == 200
    assert user.email == 'unittest2@test.com'
    


@pytest.mark.django_db
def test_user_update_password_view(client):
    
    form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
        'first_name': 'unittest',
        'middle_name': 'unittest',
        'last_name': 'unittest',
        'document': '123456789',
        'phone': '123456789',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'gender': 'unittest',
        'birthday': '1990-01-01',
    }
    
    response = client.post(
        reverse('register'),
        data=form_data
    )
    
    del form_data['password1']
    
    user = User.objects.get(**form_data)
    
    response_data = json.loads(response.content.decode('utf-8'))
    
    assert response.status_code == 200
    assert response_data['message'] == 'User created successfully.'
    assert user.email == form_data['email']
    assert user.first_name == form_data['first_name']
    assert user.middle_name == form_data['middle_name']
    assert user.last_name == form_data['last_name']
    assert user.document == form_data['document']
    assert user.phone == form_data['phone']
    assert user.street == form_data['street']
    assert user.number == form_data['number']
    assert user.city == form_data['city']
    assert user.state == form_data['state']
    assert user.country == form_data['country']
    assert user.gender == form_data['gender']
    assert user.birthday == datetime.date(1990, 1, 1)
    
    client.force_login(user)
    
    assert user.is_authenticated

    form_data = {
        'oldpassword': '123qaz123',
        'password1': '123qaz1234',
        'password2': '123qaz1234',
    }
    
    response = client.post(
        reverse('update_user_password'),
        data=form_data
    )
    # print(user.first_name)
    user.refresh_from_db()
    # print(user.first_name)
    
    assert response.status_code == 200
    assert user.check_password('123qaz1234')


@pytest.mark.django_db
def test_user_update_fields_view(client):
    
    form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
        'first_name': 'unittest',
        'middle_name': 'unittest',
        'last_name': 'unittest',
        'document': '123456789',
        'phone': '123456789',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'gender': 'unittest',
        'birthday': '1990-01-01',
    }
    
    response = client.post(
        reverse('register'),
        data=form_data
    )
    
    del form_data['password1']
    
    user = User.objects.get(**form_data)
    
    response_data = json.loads(response.content.decode('utf-8'))
    
    assert response.status_code == 200
    assert response_data['message'] == 'User created successfully.'
    assert user.email == form_data['email']
    assert user.first_name == form_data['first_name']
    assert user.middle_name == form_data['middle_name']
    assert user.last_name == form_data['last_name']
    assert user.document == form_data['document']
    assert user.phone == form_data['phone']
    assert user.street == form_data['street']
    assert user.number == form_data['number']
    assert user.city == form_data['city']
    assert user.state == form_data['state']
    assert user.country == form_data['country']
    assert user.gender == form_data['gender']
    assert user.birthday == datetime.date(1990, 1, 1)
    
    client.force_login(user)
    
    assert user.is_authenticated

    form_data = {
        'first_name': 'unittest2',
        'middle_name': 'unittest2',
        'last_name': 'unittest2',
        'document': '12345678',
        'phone': '123456789',
        'street': 'unittest2',
        'number': '123',
        'city': 'unittest2',
        'state': 'unittest2',
        'country': 'unittest2',
        'gender': 'unittest2',
        'birthday': '1990-01-01',
    }
    
    response = client.post(
        reverse('update_user_fields'),
        data=form_data
    )
    print(user.first_name)
    user.refresh_from_db()
    print(user.first_name)
    
    assert response.status_code == 200
    assert user.first_name == form_data['first_name']
    assert user.middle_name == form_data['middle_name']
    assert user.last_name == form_data['last_name']
    assert user.document == form_data['document']
    assert user.phone == form_data['phone']
    assert user.street == form_data['street']
    assert user.number == form_data['number']
    assert user.city == form_data['city']
    assert user.state == form_data['state']
    assert user.country == form_data['country']
    assert user.gender == form_data['gender']
    assert user.birthday == datetime.date(1990, 1, 1)
    