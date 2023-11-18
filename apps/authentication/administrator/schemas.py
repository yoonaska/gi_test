from rest_framework import serializers
from apps.account.models import User
from django.contrib.auth.models import Permission

class GetUserGroupsSerializer(serializers.ModelSerializer):
    
    value    =  serializers.IntegerField(source='pk')
    label    =  serializers.CharField(source='name')
    class Meta:
        model  = Permission
        fields = ['value','label'] 
        
class AdminLoginSchema(serializers.ModelSerializer):
    user_groups = serializers.SerializerMethodField('get_user_groups')
    class Meta:
        model = User
        fields = ['id','email','phone','is_active', 'user_groups']
        
    def get_user_groups(self, obj):
        return GetUserGroupsSerializer(obj.user_groups.all(), many=True).data
    
class UserAdminForgotPasswordResponseSchema(serializers.ModelSerializer):
    user_email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['user_email']