from django.urls import path, include
from employees import views

urlpatterns = [
    path('role/create/', views.CreateEmployeeRoleView.as_view(), name='create_employee_role'),
    # path('role/update/<int:pk>/', views.UpdateEmployeeRoleView.as_view(), name='update_employee_role'),
    path('update/', views.UpdateEmployeeView.as_view(), name='update_employee'),
]
