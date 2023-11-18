from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from apps.authentication.administrator.schemas import AdminLoginSchema
from apps.authentication.administrator.serializers import AdminLoginSerializer,  LogoutSerializer
from gi_test.helpers.custom_auth import EmailBackend
from gi_test.helpers.pagination import RestPagination
from gi_test.helpers.response import ResponseInfo
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics,status
from apps.account.models import User
from django.contrib import auth
from gi_test.helpers.custom_messages import _account_tem_suspended,_invalid_credentials
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
import json
from gi_test import settings
from gi_test.helpers.helpers import DataEncryption


# Create your views here.

#Start Login 
class AdminLoginView(GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(AdminLoginView, self).__init__(**kwargs)
        
    serializer_class = AdminLoginSerializer
    @swagger_auto_schema(tags=["Authorization(Admin)"])
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)

            email = serializer.validated_data.get('email', '')
            password = serializer.validated_data.get('password', '')
            
            user_instance = User.objects.get(email=email)
            if user_instance:
                
                email_backend = EmailBackend()
                user = email_backend.authenticate(request=request,username=email,password=password)

                if user:
                    serializer = AdminLoginSchema(user, context={"request": request})
                    if not user.is_active:
                        data = {'user': {}, 'token': '', 'refresh': ''}
                        self.response_format['status_code'] = status.HTTP_202_ACCEPTED
                        self.response_format["data"] = data
                        self.response_format["status"] = False
                        self.response_format["message"] = _account_tem_suspended
                        return Response(self.response_format, status=status.HTTP_200_OK)
                    else:
                        final_out         = json.dumps(serializer.data)
                        secret_key  = settings.E_COMMERCE_SECRET
                        key         = secret_key
            
                        encrypted_data    = DataEncryption.encrypt(key, final_out)
                        access_tokens = AccessToken.for_user(user)
                        refresh_token = RefreshToken.for_user(user)             

                        data = {'user': encrypted_data, 'token': str(access_tokens), 'refresh': str(refresh_token)}
                        self.response_format['status_code'] = status.HTTP_200_OK
                        self.response_format["data"] = data
                        self.response_format["status"] = True

                        return Response(self.response_format, status=status.HTTP_200_OK)
                else:
                    self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                    self.response_format["message"] = _invalid_credentials
                    self.response_format["status"] = False
                    return Response(self.response_format, status=status.HTTP_401_UNAUTHORIZED)

            else:
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["message"] = _invalid_credentials
                self.response_format["status"] = False
                return Response(self.response_format, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            self.response_format['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status'] = False
            self.response_format['message'] = str(e)
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# End Login


# Start Log Out
class LogoutAPIView(GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(LogoutAPIView, self).__init__(**kwargs)
        
    serializer_class = LogoutSerializer
    # permission_classes = (IsAuthenticated,)
    
    @swagger_auto_schema(tags=["Authorization(Admin)"])
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
          
            self.response_format['status'] = True
            self.response_format['status_code'] = status.HTTP_200_OK
            return Response(self.response_format, status=status.HTTP_200_OK)
        except Exception as e:
            self.response_format['status'] = False
            self.response_format['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['message'] = str(e)
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
   
        
