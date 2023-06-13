from companys.models import Company
from users.models import User

def company_create(validated_data, user: User) -> Company:
    company = Company(**validated_data)
    company.set_root(user=user)
    user.employee.set_company(company)
    return company