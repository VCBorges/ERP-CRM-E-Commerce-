from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer

import traceback
from typing import Literal


class BaseCreateAPIViewMixin:
    
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

    
    def serializer_methods(self, serializer: Serializer, *args, **kwargs) -> None:
        serializer.save()
        
        
    def get_valid_response_data(self, serializer: Serializer, *args, **kwargs) -> dict:
        valid_data = {'data': serializer.data}
        return valid_data
    
    def get_invalid_response_data(self, serializer: Serializer, *args, **kwargs) -> dict:
        invalid_data = {'data': serializer.errors}
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
        try:
            serializer = self.get_serializer()
            if serializer.is_valid():
                self.serializer_methods(serializer=serializer)
                response = self.get_response(
                    data=self.get_valid_response_data(serializer=serializer),
                    status_code=status.HTTP_201_CREATED
                )
            else:
                response = self.get_response(
                    data=self.get_invalid_response_data(serializer=serializer),
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            traceback.print_exc()
            response = self.get_response(
                data=self.get_server_error_response_data(error=e),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        finally:
            return response
        


class BaseAuthMixin:
    
    authentication_classes = (
        BasicAuthentication,
        TokenAuthentication,
    )