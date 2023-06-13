from rest_framework import serializers

from companys.models import Company
from companys.services import company_create

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=255)
    website = serializers.CharField(max_length=255)
    document = serializers.CharField(max_length=255)
    # industry = serializers.CharField(max_length=255)
    # size = serializers.CharField(max_length=255)
    # street = serializers.CharField(max_length=255)
    # number = serializers.CharField(max_length=255)
    # city = serializers.CharField(max_length=255)
    # state = serializers.CharField(max_length=255)
    # country = serializers.CharField(max_length=255)
    # postal_code = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        # print(self.context.user)
        return
        # return company_create(validated_data, self.context['request'].user)
    
        
    def update(self, instance, validated_data):
        for field in validated_data:
            setattr(instance, field, validated_data[field])
        instance.save()
        return instance
    
    
    def validate(self, data):
        if self.context['request'].user.is_root:
            raise serializers.ValidationError(
                "User already is company's root"
            )
        if self.context['request'].user.employee.company:
            raise serializers.ValidationError(
                'Employee already has a company'
            )
        return data
    