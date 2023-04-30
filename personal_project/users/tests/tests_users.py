from django.urls import reverse
from django.test import RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware

from users import views


import json
import pytest




@pytest.mark.django_db
def test_user_registration_view(client):
    # Create a request object and pass it to the view
    factory = RequestFactory()

    form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
    }

    # Create a POST request with the form data
    request = factory.post(reverse('register'), data=form_data)

    middleware = SessionMiddleware(get_response=lambda r: None)
    middleware.process_request(request)
    
    response = views.UserRegistrationView.as_view()(request)
    
    # print
    # Check that the response has the correct status code and message
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    print(response_data)
    print(response_data['message'])
    assert response_data['message'] == 'User created successfully.'