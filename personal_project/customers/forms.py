from typing import Any, Dict
from django import forms

from core.formsmixins import RequestFormMixin
from core.formsmixins import UpdateRequestFormMixin
from customers.models import Customer
from core.utils import set_model_instance_fields



class CreateCustomerForm(
    RequestFormMixin,
    forms.ModelForm
):
    
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'document',
            'email',
            'website',
        ]
        
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)       
    #     super().__init__(*args, **kwargs)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     if not name:
    #         raise forms.ValidationError('Name field is required2.')
    #     return cleaned_data
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Name field is required.')
        return name
    
    
    
    # def clean_document(self):
    #     document = self.cleaned_data.get('document')
    #     if not document:
    #         raise forms.ValidationError('Document field is required.')
    #     return document
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email:
    #         raise forms.ValidationError('Email field is required.')
    #     return email


    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone:
    #         raise forms.ValidationError('Phone field is required.')
    #     return phone
    
    # def save(self, commit=True):
    #     instance = super().save(commit=False)
    #     instance.company = self.request.user.company
    #     instance.company_name = self.request.user.company.name
    #     instance.save()
    #     return instance
        
    
    
        
        
class UpdateCustomerForm(
    UpdateRequestFormMixin,
    forms.ModelForm
):
    class Meta:
        model = Customer
        fields = [
            'name',
            'email',
            'phone',
            'address',
            'document',
        ]
    
    
    # def clean(self) -> Dict[str, Any]:
    #     cleaned_data = super().clean()
    #     try:
    #         self.instance = Customer.objects.get(
    #             pk=self.pk
    #         )
    #     except Customer.DoesNotExist:
    #         raise forms.ValidationError('Customer does not exist.')
    #     return cleaned_data
    
    
    # def save(self, commit: bool = True):
    #     instance = Customer.objects.get(pk=self.pk)
    #     set_instance_updated_fields(
    #         instance=instance, 
    #         cleaned_data=self.cleaned_data
    #     )
    #     if commit:
    #         instance.save()
            
    #     return instance
        
        
        
        