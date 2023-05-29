from django.forms import ModelForm
from django.forms import Form
from django.db.models import Model
from django.http import HttpRequest

from employees.models import Employee
from companys.models import Company
from users.models import User


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


def get_current_employee(request: HttpRequest) -> Employee:
    return request.user.employee


def get_root_user_company_from_request(request: HttpRequest) -> Company | None:
    return request.user.get_root_company()


def get_current_user(request: HttpRequest) -> User:
    return request.user


def get_current_employee_company(request: HttpRequest) -> Company | None:
    try:
        return request.user.employee.company
    except Company.DoesNotExist:
        return None
    

def current_employee_has_company(request: HttpRequest) -> bool:
    if get_current_employee_company(request):
        return True
    return False


def current_user_is_root(request: HttpRequest) -> bool:
    if request.user.is_root():
        return True
    return False

    
def set_current_employee_company(request: HttpRequest, company: Company) -> Employee:
    request.user.employee.set_company(company)
    return request.user.employee