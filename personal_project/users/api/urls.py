from django.urls import path
# from companys.api import views
from users.api import views

urlpatterns = [
    path('register/', views.UserRegistrationAPI.as_view(), name='register_user'),
    path('login/process/', views.LoginView.as_view(), name='login_user'),
]

