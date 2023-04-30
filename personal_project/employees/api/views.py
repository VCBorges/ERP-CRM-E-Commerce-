from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin
from django.views.decorators.csrf import ensure_csrf_cookie

from personal_project.core.apiviews import DataTableAPIView
from employees.models import Employee
from employees.api.datatable import EmployeeDataTable
from employees.api.serializers import EmployeeSerializer



class EmployeeDataTableAPIView(DataTableAPIView):
    
    queryset = Employee.objects.all()
    datatable_class = EmployeeDataTable
    serializer_class = EmployeeSerializer
