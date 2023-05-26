from django.http import HttpRequest

from employees.models import Employee
from companys.models import Company
from users.models import User




def get_employee_from_request(request: HttpRequest) -> Employee:
    return request.user.employee


def get_root_user_company_from_request(request: HttpRequest) -> Company | None:
    return request.user.get_root_company()


def get_user_from_request(request: HttpRequest) -> User:
    return request.user


def get_employee_company_from_request(request: HttpRequest) -> Company | None:
    try:
        return request.user.employee.company
    except Company.DoesNotExist:
        return None
    

def employee_has_company(request: HttpRequest) -> bool:
    if get_employee_company_from_request(request):
        return True
    return False


def user_is_root(request: HttpRequest) -> bool:
    if request.user.is_root():
        return True
    return False


# def set_company_root(request: HttpRequest, company: Company) -> Company:
#     company.root = request.user
#     return company
    
    

def set_employee_company(request: HttpRequest, company: Company) -> Employee:
    request.user.employee.set_company(company)
    return request.user.employee
    