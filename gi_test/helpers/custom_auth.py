# your_app/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        
class PhoneOTPBackend(ModelBackend):
    def authenticate(self, request, phone_number=None, otp=None, **kwargs):
        try:
            user = User.objects.get(phone=phone_number) 
            return user
        except User.DoesNotExist:
            return None

        # if TOTPDevice.verify_is_valid(user, otp):
        #     return user      
          
class EmailOTPBackend(ModelBackend):
    def authenticate(self, request, email=None, otp=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None