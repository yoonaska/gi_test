# from rest_framework import serializers
# from apps.account.models import User
# from django_acl.models import Group
# from apps.permissions.models import Roles, Groups
# from gi_test.helpers.helpers import get_object_or_none
# from django.contrib.auth.models import Permission

# class RegistrationSerializer(serializers.ModelSerializer):
#     instance_id   = serializers.PrimaryKeyRelatedField(required=False,queryset=User.objects.all(),default=None)
#     first_name       = serializers.CharField(required=True)
#     last_name        = serializers.CharField(required=True)
#     email            = serializers.EmailField(required=True)
#     phone            = serializers.CharField(required=True)
#     groups           = serializers.PrimaryKeyRelatedField(read_only=False, many=True, queryset=Groups.objects.all(), required=False) 
    
#     class Meta:
#         model  = User
#         fields = ['instance_id', 'first_name', 'last_name', 'email', 'phone', 'groups']
        
#     def validate(self, attrs):
     
#         phone    = attrs.get('phone')
#         email    = attrs.get('email')
#         instance_id    = attrs.get('instance_id')
        
#         if not instance_id:
#             if phone and email and User.objects.filter(phone=phone, email=email).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that phone number and email address is already in exists!']
#                                                 })
            
#             if phone and User.objects.filter(phone=phone).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that phone number already exists!']})


#             if email and User.objects.filter(email=email).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that email address already exists!']})
            
#             return super().validate(attrs)
#         else:
#             if phone and email and User.objects.filter(phone=phone, email=email).exclude(id=instance_id.id).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that phone number and email address is already in exists!']
#                                                 })
            
#             if phone and User.objects.filter(phone=phone).exclude(id=instance_id.id).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that phone number already exists!']})


#             if email and User.objects.filter(email=email).exclude(id=instance_id.id).exists():
#                 raise serializers.ValidationError({"error": ['Sorry, that email address already exists!']})
            
#             return super().validate(attrs)
    
#     def create(self, validated_data):
#         request = self.context.get('request')
#         instance              = User()
#         instance.first_name   = validated_data.get('first_name',None)
#         instance.last_name    = validated_data.get('last_name',None)
#         instance.phone        = validated_data.get('phone',None)
#         instance.email        = validated_data.get('email',None)
#         instance.is_admin     = True
#         groups                = validated_data.pop('groups',None)
#         instance.save()
        
        
#         # assigning groups
#         # if groups is not None:
#         #     for group_instance in groups:
#         #         if group_instance is not None:
                    
#         #             group_instance.user.add(instance)
#         #             # group_instance.user_set.add(instance)
#         # return instance

#     def update(self, instance, validated_data):
        
#         # groups        = validated_data.pop('groups',None)

#         # active_groups = instance.user_groups.all().values_list('id',flat=True)
                
#         # remove_groups = [item for item in active_groups if str(item) not in groups]
        
#         # [groups.remove(str(item)) for item in active_groups if str(item) in groups]
        
#         request               = self.context.get('request')
#         instance.first_name   = validated_data.get('first_name',None)
#         instance.last_name    = validated_data.get('last_name',None)
#         instance.phone        = validated_data.get('phone',None)
#         instance.email        = validated_data.get('email',None)
#         groups                = validated_data.pop('groups',None)
#         instance.save()
        
#         # if remove_groups:
#         #     for remove_group in remove_groups:
#         #         remove_group_instance = get_object_or_none(Groups,id=remove_group)
#         #         if remove_group_instance is not None:
#         #             remove_group_instance.custom_user_set.remove(instance)

#         # if instance is not None:
#         #     if groups:
#         #         for group_instance in groups:
#         #             if group_instance is not None:
#         #                 group_instance.custom_user_set.add(instance)
        
#         return instance
    

# class ActiveOrInactivateAdminProfileSerializer(serializers.ModelSerializer):
#     instance_id   = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),default=None)
    
#     class Meta:
#         model = User
#         fields = ['instance_id']
        
#     def validate(self, attrs):
#         return super().validate(attrs)

#     def update(self, instance , validated_data):
#         instance.is_active = True if not instance.is_active else False
#         instance.save()
#         return instance
    

# class GetUserGroupsSerializer(serializers.ModelSerializer):
    
#     value    =  serializers.IntegerField(source='pk')
#     label    =  serializers.CharField(source='name')
#     class Meta:
#         model  = Permission
#         fields = ['value','label'] 
        
# class GetUsersResponseSchemas(serializers.ModelSerializer):
    
#     # user_groups = serializers.SerializerMethodField('get_user_groups')
#     class Meta:
#         model = User
#         fields = ['id','first_name','last_name', 'email', 'phone','is_admin','is_active','is_superuser',]
        
#     # def get_user_groups(self,obj):
#     #     return GetUserGroupsSerializer(obj.user_groups.all(), many=True).data
    
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         for field in data:
#             try:
#                 if data[field] is None:
#                     data[field] = ""
#             except KeyError:
#                 pass
#         return data