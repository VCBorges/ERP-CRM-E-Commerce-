from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions

# from braces.views import CsrfExemptMixin
# from rest_framework.mixins import 

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.api.serializers import CompanySerializer
# APIView

class CreateCompanyAPI(APIView):
    
    # permission_classes = (permissions.AllowAny)
    # authentication_classes = (BasicAuthentication,)
    # csrf_exempt = True
    
    def post(self, request, format=None):
        print(f'User: {request.user}')
        serializer = CompanySerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, format=None):
        print(f'User: {request.user}')
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)
    # def enforce_csrf(self, request):
    #     pass
    
    def enforce_csrf(self, request):
        return