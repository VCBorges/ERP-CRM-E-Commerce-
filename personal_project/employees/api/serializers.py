from rest_framework import serializers

from employees.models import Employee
from employees.api.datatable import EmployeeDataTable

class EmployeeSerializer(serializers.ModelSerializer):
    
    # name = serializers.CharField(required=True)
    # status = serializers.CharField(required=True)
    # document = serializers.CharField(required=False)
    # email = serializers.CharField(required=False)
    # phone = serializers.CharField(required=False)
    # address = serializers.CharField(required=False)
    # website = serializers.CharField(required=False)
    # company = serializers.CharField(required=False)
    
    teste = serializers.SerializerMethodField()
    # index = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = EmployeeDataTable.columns + ['teste']
    
    def validate_name(self, value):
        
        """
        #*Check that the movie name is not too similar to another movie.
        """
        
        if value == 'abc':
            raise serializers.ValidationError('Movie name is not unique.')
        return value
    
    def validate_status(self, value):
        
        """
        #*Check that the movie name is not too similar to another movie.
        """
        
        if value == 'abc':
            raise serializers.ValidationError('Movie name is not unique.')
        return value
    
    def get_teste(self, obj):
        return 'teste'
    
    # def get_index(self, obj):
    #     """
    #     Returns the index of the object in the queryset
    #     """
    #     queryset = self.context['view'].get_queryset()
    #     print(queryset)
    #     index = queryset.index(obj)
    #     return index