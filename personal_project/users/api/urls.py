from django.urls import path
# from companys.api import views
from users.api import views

urlpatterns = [
    path('register/', views.UserRegistrationAPI.as_view(), name='register_user'),
    path('login/process/', views.LoginView.as_view(), name='login_user'),
    path('logout/process/', views.UserLogoutAPI.as_view(), name='logout_user'),
    path('update/email/', views.UpdateUserEmailAPI.as_view(), name='update_user_email'),
    path('update/password/', views.UpdateUserPasswordAPI.as_view(), name='update_user_password'),
    path('update/', views.UpdateUserFieldsAPI.as_view(), name='update_user_fields'),
]

