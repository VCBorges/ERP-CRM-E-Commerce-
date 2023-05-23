from django.http import HttpRequest

from employees.models import Employee
from companys.models import Company
from users.models import User



def get_employee_from_request(request: HttpRequest) -> Employee:
    return request.user.employee


def set_employees_company(request: HttpRequest, company) -> Employee:
    employee = get_employee_from_request(request)
    employee.company = company
    return employee


def employee_has_company(request: HttpRequest) -> bool:
    return get_employee_from_request(request).company is not None


def get_user_company(user: User) -> Company:
    try:
        return user.company
    except Company.DoesNotExist:
        return None



def get_user_company_from_request(request: HttpRequest) -> Company:
    return get_user_company(request.user)


def get_user_from_request(request: HttpRequest) -> User:
    return request.user



def user_has_company(request: HttpRequest) -> bool:
    if get_user_company(user=request.user) is None:
        return False
    return True