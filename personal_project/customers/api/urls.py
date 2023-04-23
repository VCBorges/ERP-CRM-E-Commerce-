from django.urls import path

from customers.api import views

urlpatterns = [
    path('datatable/', views.CustomerDataTableAPIView.as_view(), name='customers_datatable'),
]
