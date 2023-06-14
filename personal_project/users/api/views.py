from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions

from dj_rest_auth.views import LoginView


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.api.serializers import CompanySerializer
from users.api.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
)
from core.apiviews import BaseCreateAPIView


import traceback



class UserRegistrationAPI(BaseCreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def serializer_methods(self, serializer: Serializer, *args, **kwargs) -> None:
        serializer.save(request=self.request)


# class UserRegistrationAPI(APIView):
    
#     # permission_classes = (permissions.AllowAny)
#     # authentication_classes = (BasicAuthentication,)
#     # csrf_exempt = True
    
#     def post(self, request, format=None):
#         try:
#             serializer = UserRegistrationSerializer(
#                 data=request.data,
#             )
#             if serializer.is_valid():
#                 serializer.save(request=request)
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             print(f'Error: {str(e)}')
#             traceback.print_exc()
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
#     def get(self, request, format=None):
#         print(f'User: {request.user}')
#         print(f'Headers: {request.headers}')
#         return Response({'hello': 'world'}, status=status.HTTP_200_OK)


# my_tuple = ('1')
# print(my_tuple) 
# print(type(my_tuple))

class UserLoginAPI(APIView):
    
    def post(self, request, format=None):
        try:
            # print(f'User: {request.user}')
            serializer = UserLoginSerializer(
                data=request.data,
                context={'request': request}
            )
            if serializer.is_valid():
                serializer.save(request=request)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f'Error: {str(e)}')
            traceback.print_exc()
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def get(self, request, format=None):
        print(f'User: {request.user}')
        return Response({'hello': 'world'}, status=status.HTTP_200_OK)