from django.forms import ModelForm
from django.forms import Form



def get_form_errors(form: ModelForm | Form) -> list[str]:
    
    '''
    Returns a list of errors from a form.
    '''
    
    error_list = [
        f"{field}: {error}" 
            for field, errors in form.errors.items() 
                for error in errors
    ]
    return error_list