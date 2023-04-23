from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin
from django.views.decorators.csrf import ensure_csrf_cookie

from customers.models import Customer
from customers.api.datatable import CustomerDataTable
from customers.api.serializers import CustomerSerializer
from core.apiviewsmixins import DataTableAPIView


class CustomerDataTableAPIView(DataTableAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
    queryset = Customer.objects.all()
    datatable_class = CustomerDataTable
    serializer_class = CustomerSerializer