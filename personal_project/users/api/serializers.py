from django.contrib.auth import get_user_model

from django.db import transaction
from employees.models import Employee
from core.utils import (
    set_fields_model_instance,
    update_instance_fields,
    get_current_user,
)

from allauth.account.models import EmailAddress
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer

USER = get_user_model()

from dj_rest_auth.serializers import PasswordChangeSerializer




class UserRegistrationSerializer(RegisterSerializer):

    first_name = serializers.CharField(required=True)
    middle_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=True)
    document = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    street = serializers.CharField(required=False)
    number = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    gender = serializers.CharField(required=False)
    group = serializers.ChoiceField(choices=USER.Groups.choices, required=False)


    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['first_name'] = self.validated_data.get('first_name', '')
        cleaned_data['middle_name'] = self.validated_data.get('middle_name', '')
        cleaned_data['last_name'] = self.validated_data.get('last_name', '')
        cleaned_data['document'] = self.validated_data.get('document', '')
        cleaned_data['phone'] = self.validated_data.get('phone', '')
        cleaned_data['street'] = self.validated_data.get('street', '')
        cleaned_data['number'] = self.validated_data.get('number', '')
        cleaned_data['city'] = self.validated_data.get('city', '')
        cleaned_data['state'] = self.validated_data.get('state', '')
        cleaned_data['country'] = self.validated_data.get('country', '')
        cleaned_data['birthday'] = self.validated_data.get('birthday', '')
        cleaned_data['gender'] = self.validated_data.get('gender', '')
        cleaned_data['group'] = self.validated_data.get('group', '')
        return cleaned_data
    
    
    def save(self, request):
        user = super().save(request)
        try:
            set_fields_model_instance(
                instance=user, 
                cleaned_data=self.cleaned_data
            )
            Employee.objects.create(
                user=user,
            )
            user.save()
        except:
            user.emailaddress_set.all().delete()
            user.delete()
            raise Exception("Error creating user.")
        return user
    
    
class UserLoginSerializer(LoginSerializer):
    pass
    ...
    
    
class UpdateUserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        if self.context['request'].user.email == value:
            raise serializers.ValidationError('The email was not changed.')
        if EmailAddress.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists.')
        return value


    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.context['request'].user:
            raise serializers.ValidationError('No user')
        return attrs


    def save(self):
        user = get_current_user(self.context['request'])
        user.email = self.validated_data['email']
        with transaction.atomic():
            user.save()
            user.emailaddress_set.filter(primary=1).update(email=self.validated_data['email'])
        return user
    
    
class UpdateUserPasswordSerializer(PasswordChangeSerializer):
    pass



class UpdateUserFieldsSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    middle_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    document = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    street = serializers.CharField(required=False)
    number = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    gender = serializers.CharField(required=False)
    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        if not self.context['request'].user:
            raise serializers.ValidationError('No user')
        return attrs
    
    def save(self):
        user = get_current_user(self.context['request'])
        with transaction.atomic():
            update_instance_fields(
                instance=user, 
                data=self.validated_data
            )
            user.save()
        return user
    
    