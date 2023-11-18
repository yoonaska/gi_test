from rest_framework import serializers
from apps.account.models import User
from django.contrib.auth.models import Permission
from django_acl.models import Group


class RegistrationSchema(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone']
        
        

class GetUserGroupsSerializer(serializers.ModelSerializer):
    
    value    =  serializers.IntegerField(source='pk')
    label    =  serializers.CharField(source='name')
    class Meta:
        model  = Group
        fields = ['value','label'] 
        
class GetUsersResponseSchemas(serializers.ModelSerializer):
    
    user_groups = serializers.SerializerMethodField('get_user_groups')
    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'email', 'phone','is_admin','is_active','is_superuser', 'user_groups']
        
    def get_user_groups(self,instance):
        groups = instance.user_groups.all()        
        return GetUserGroupsSerializer(groups, many=True).data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in data:
            try:
                if data[field] is None:
                    data[field] = ""
            except KeyError:
                pass
        return data