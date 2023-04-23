from django.urls import path, include
from customers.views import CustomerCreateView
from customers.views import CustomerTemplateView

urlpatterns = [
    path('api/', include('customers.api.urls')),
     
    path('', CustomerTemplateView.as_view(), name='customers'),
    path('create/', CustomerCreateView.as_view(), name='create_customer'),
]
