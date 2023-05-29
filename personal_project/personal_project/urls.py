from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('customers/', include('customers.urls')),
    path('users/', include('users.urls')),
    # path('company/', include('companys.urls')),
    # path('employee/', include('employees.urls')),
]
