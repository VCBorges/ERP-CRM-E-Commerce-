from django.urls import path, include
from users import views

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('loginS/', views.LoginTemplateView.as_view(), name='login_template'),
]
