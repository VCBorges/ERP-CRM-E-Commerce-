from django.http import HttpRequest

from employees.models import Employee
from companys.models import Company
from users.models import User



# def get_current_employee(request: HttpRequest) -> Employee:
#     return request.user.employee


# def get_current_root_company(request: HttpRequest) -> Company | None:
#     return request.user.root_company


# def get_current_user(request: HttpRequest) -> User:
#     return request.user


# def get_current_employee_company(request: HttpRequest) -> Company | None:
#     try:
#         return request.user.employee.company
#     except Company.DoesNotExist:
#         return None
    

# def current_employee_has_company(request: HttpRequest) -> bool:
#     if get_current_employee_company(request):
#         return True
#     return False


# def current_user_is_root(request: HttpRequest) -> bool:
#     if request.user.is_root():
#         return True
#     return False

    
# def set_current_employee_company(request: HttpRequest, company: Company) -> Employee:
#     request.user.employee.set_company(company)
#     return request.user.employee
    