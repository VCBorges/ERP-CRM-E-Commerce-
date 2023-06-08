from django import forms
from core.utils import get_model_verbose_name
from core.utils import update_instance_fields

from django.views.generic import UpdateView





class RequestKwargFormMixin:
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)       
        super().__init__(*args, **kwargs)
        
        


class PkRequestKwargsFormMixin(RequestKwargFormMixin):
    
    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk', None)
        super().__init__(*args, **kwargs)
    
        
    def clean(self):
        cleaned_data = super().clean()
        try:
            self.object = self.Meta.model.objects.get(
                pk=self.pk
            )
        except self.Meta.model.DoesNotExist:
            raise forms.ValidationError(
                f'{get_model_verbose_name(self.Meta.model)} does not exist.'
            )
        return cleaned_data
    
    
    
    def save(self, commit: bool = True):
        update_instance_fields(
            instance=self.object, 
            data=self.cleaned_data
        )
        if commit:
            self.object.save()
            
        return self.object