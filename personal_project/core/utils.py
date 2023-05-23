from django.forms import ModelForm
from django.forms import Form
from django.db.models import Model

from datetime import datetime

def get_form_errors(form: ModelForm | Form) -> list[str]:
    
    '''
    Returns a list of errors from a form.
    '''
    
    error_list = [
        f"{field}: {error}" 
            for field, errors in form.errors.items() 
                for error in errors
    ]
    return {
        'errors': error_list
    }
    
    

def get_model_verbose_name(model: Model) -> str:
    
    '''
    Returns the verbose name of a model.
    '''
    
    return model._meta.verbose_name.title()




def set_model_instance_fields(instance: Model, cleaned_data: dict, *args, **kwargs) -> None:
    for field in instance._meta.fields:
        value = cleaned_data.get(field.name)
        setattr(instance, field.name, value)
        
        

def set_fields_model_instance(instance: Model, cleaned_data: dict, *args, **kwargs) -> None:
    del cleaned_data['email']
    del cleaned_data['password1']
    for key,value in cleaned_data.items():
        if value:
            setattr(instance, key, value)
        
        
def get_today() -> datetime:
    return datetime.today()


def get_now() -> datetime:
    return datetime.now()