from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

from users.models import User
from employees.models import Employee
from core.factories import set_session_middleware
from users import views


import json
import pytest
import datetime




@pytest.mark.django_db
def test_user_registration_view(client):
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

    response = views.UserRegistrationView.as_view()(
        set_session_middleware(request)
    )
    
    del form_data['password1']
    
    user = User.objects.get(**form_data)
    employee = Employee.objects.get(user=user)
    
    response_data = json.loads(response.content.decode('utf-8'))
    
    assert response.status_code == 200
    assert response_data['message'] == 'User created successfully.'
    assert user.email == 'unittest@test.com'
    assert user.first_name == 'unittest'
    assert user.middle_name == 'unittest'
    assert user.last_name == 'unittest'
    assert user.document == '123456789'
    assert user.phone == '123456789'
    assert user.street == 'unittest'
    assert user.number == '123'
    assert user.city == 'unittest'
    assert user.state == 'unittest'
    assert user.country == 'unittest'
    assert user.gender == 'unittest'
    assert user.birthday == datetime.date(1990, 1, 1)
    
    assert employee.work_email == 'unittest@test.com'
    assert employee.work_phone == '123456789'