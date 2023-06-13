from django.urls import path, include
from companys import views

urlpatterns = [
    # path('', views.CompanyTemplateView.as_view(), name='company'),
    path('api/', include('companys.api.urls')),
    path('create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('update/', views.UpdateCompanyView.as_view(), name='company_update'),
]
