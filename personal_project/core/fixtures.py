from django.urls import reverse

from users.models import User
from companys.models import Company


import pytest
import json
import pytest
import datetime


@pytest.fixture
def auto_create_login_user(client):
   def make_auto_login(user=None):
       if user is None:
           
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
       return client, user
   return make_auto_login



@pytest.fixture
def auto_create_company_login_user(auto_create_login_user):
   def make_auto_login(user=None):
       if user is None:
           
            client, user = auto_create_login_user()
           
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

       client.force_login(user)
       assert user.is_authenticated
       return client, user, company
   return make_auto_login