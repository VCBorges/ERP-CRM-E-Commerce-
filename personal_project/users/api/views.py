from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import permissions
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated

from dj_rest_auth.views import LoginView, LogoutView
# dj_rest_auth.serializers.PasswordChangeSerializer
# from dj_rest_auth.registration.views import RegisterView

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from companys.api.serializers import CompanySerializer
from users.api.serializers import (
    UserRegistrationSerializer,
    UpdateUserEmailSerializer,
    UpdateUserPasswordSerializer,
    UpdateUserFieldsSerializer,
)
from core.apiviews import (
    BaseCreateAPIView,
    BaseUpdateUserAPIView,
)




class UserRegistrationAPI(BaseCreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def serializer_methods(self, serializer: Serializer, *args, **kwargs) -> None:
        serializer.save(request=self.request)


class UpdateUserEmailAPI(BaseUpdateUserAPIView):
    serializer_class = UpdateUserEmailSerializer
    
    
class UpdateUserPasswordAPI(BaseUpdateUserAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserPasswordSerializer
    
    def get_valid_response_data(self, *args, **kwargs) -> dict:
        return {'detail': 'Password updated successfully.'}
    

class UserLogoutAPI(LogoutView):
    pass


class UpdateUserFieldsAPI(BaseUpdateUserAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserFieldsSerializer
    