from django.urls import reverse
from django.test import RequestFactory

from customers.views import CustomerCreateView


import json
import pytest


# @pytest.mark.django_db
# def test_customers_template_view(client):
#     response = client.get(reverse('customers'))
#     assert response.status_code == 200
#     print(response.content)
#     assert b'Customers' in response.content
    
    

@pytest.mark.django_db
def test_create_customer_view(client):
    # Create a request object and pass it to the view
    factory = RequestFactory()

    form_data = {
        'name': 'John Doe',
    }

    # Create a POST request with the form data
    request = factory.post(reverse('create_customer'), data=form_data)
    response = CustomerCreateView.as_view()(request)
    

    # Check that the response has the correct status code and message
    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data['message'] == 'Customer created successfully.'