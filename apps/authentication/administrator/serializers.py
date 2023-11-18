from apps.account.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.hashers import make_password, check_password
# Start Login
class AdminLoginSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['email','password']
    
    def validate(self, attrs):
        return super().validate(attrs)    
    
# End Login


# Start Logout
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            return self.fail('bad_token')
        
# End Logout


