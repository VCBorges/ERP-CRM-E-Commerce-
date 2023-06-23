from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from core.datatables import DataTableServerSide
from core.datatables import DataTableServerSideDRF
from core.apiviewsmixins import (
    BaseCreateAPIMixin,
    BaseUpdateUserAPIMixin,
    BaseAuthMixin,
)



class DataTableAPIView(ListModelMixin, GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # queryset = Customer.objects.all()
   
    queryset: QuerySet = None
    datatable_class: DataTableServerSide | DataTableServerSideDRF = None
    serializer_class: ModelSerializer = None
    
    
    def get_queryset(self):
        self.datatable: DataTableServerSide | DataTableServerSideDRF = self.datatable_class(
            request=self.request,
            queryset=self.queryset,
        )
        # print(self.datatable.get_queryset())
        return self.datatable.get_filtered_queryset()

    
    
    def post(self, request, format=None):
        return self.list(request)
    
    
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_queryset(),
            many=True
        )
        
        # serializer_data_sorted = sorted(serializer.data, key=lambda x: x['id'], reverse=True)
        # serializer_data_sorted = sorted(serializer.data, key=lambda x: x['id'])
        
        response = self.datatable.get_response(
            serialized_data=serializer.data
        )
        return Response(response)
    
    

class BaseCreateAPIView(
    BaseAuthMixin,
    BaseCreateAPIMixin,
    APIView,
):
    DEBUG: bool = True
    
    
class BaseUpdateUserAPIView(
    BaseAuthMixin,
    BaseUpdateUserAPIMixin,
    APIView,
):
    DEBUG: bool = True
    allowed_methods = ['PUT']
    http_method_names = ['put']
