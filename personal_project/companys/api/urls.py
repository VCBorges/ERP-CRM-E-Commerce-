from django.urls import path
from companys.api import views

urlpatterns = [
    # path('', views.CompanyTemplateView.as_view(), name='company'),
    path('create/', views.CreateCompanyAPI.as_view(), name='create_company'),
    # path('update/', views.UpdateCompanyView.as_view(), name='company_update'),
]

