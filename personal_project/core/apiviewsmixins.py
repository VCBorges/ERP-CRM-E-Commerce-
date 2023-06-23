from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from dj_rest_auth.views import PasswordChangeView
# from django.utils.translation import gettext_lazy as _

import traceback
from typing import Literal



class BaseCreateAPIMixin:
    
    serializer_class: Serializer = None
    
    def get_serializer_context(self, *args, **kwargs) -> dict:
        context = {'request': self.request}
        return context

    def get_serializer_kwargs(self, *args, **kwargs) -> dict:
        kwargs['data'] = self.request.data
        kwargs['context'] = self.get_serializer_context()
        return kwargs


    def get_serializer(self, *args, **kwargs) -> Serializer:
        serializer = self.serializer_class(
            **self.get_serializer_kwargs()
        )
        return serializer

    
    def serializer_methods(self, *args, **kwargs) -> None:
        self.serializer.save()
        
        
    def get_valid_response_data(self, *args, **kwargs) -> dict:
        valid_data = {'data': self.serializer.data}
        return valid_data
    
    
    def get_invalid_response_data(self, *args, **kwargs) -> dict:
        invalid_data = {'data': self.serializer.errors}
        return invalid_data
    
    
    def get_server_error_response_data(self, error: Exception, *args, **kwargs) -> dict:
        server_error_data = {'error': str(error)}
        return server_error_data 
    
    
    def get_response(self, data: dict, status_code: Literal, *args, **kwargs) -> Response:
        response = Response(
            data=data,
            status=status_code
        )
        return response
    
    
    def post(self, request, format=None):
        self.request = request
        if self.DEBUG:
            print(self.request.data)
        try:
            self.serializer = self.get_serializer()
            if self.serializer.is_valid():
                self.serializer_methods()
                response = self.get_response(
                    data=self.get_valid_response_data(serializer=self.serializer),
                    status_code=status.HTTP_201_CREATED
                )
            else:
                if self.DEBUG:
                    print(f'Serializer errors: {self.serializer.errors}')
                response = self.get_response(
                    data=self.get_invalid_response_data(serializer=self.serializer),
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            if self.DEBUG:
                traceback.print_exc()
            response = self.get_response(
                data=self.get_server_error_response_data(error=e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        finally:
            return response
        


class BaseUpdateUserAPIMixin(BaseCreateAPIMixin):
    def put(self, request, format=None):
        return self.post(request, format=format)


class BaseAuthMixin:
    
    authentication_classes = (
        BasicAuthentication,
        TokenAuthentication,
    )