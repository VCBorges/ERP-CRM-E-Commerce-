from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import permissions

# from rest_auth.views import LoginView

# from braces.views import CsrfExemptMixin
# from rest_framework.mixins import 

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.api.serializers import CompanySerializer
# APIView
from core.apiviews import BaseCreateAPIView

import traceback

class CreateCompanyAPI(BaseCreateAPIView):

    serializer_class = CompanySerializer