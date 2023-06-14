from django.urls import path, include
from users import views
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('api/', include('users.api.urls')),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/process/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('login/', views.LoginTemplateView.as_view(), name='login_template'),
    path('update/email/', views.UpdateUserEmailView.as_view(), name='update_user_email'),
    path('update/password/', views.UpdateUserPasswordView.as_view(), name='update_user_password'),
    path('update/fields/', views.UpdateUserFieldsView.as_view(), name='update_user_fields'),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),

]