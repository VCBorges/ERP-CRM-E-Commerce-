from django.urls import path
from companys import views

urlpatterns = [
    path('', views.CompanyTemplateView.as_view(), name='company'),
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
]
