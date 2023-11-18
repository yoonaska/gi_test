from rest_framework import serializers
from apps.account.models import User
from gi_test.helpers.helpers import get_object_or_none
from django.contrib.auth.models import Permission
import os, sys, logging
from django_acl.models import Group, Role

logger = logging.getLogger(__name__)

class RegistrationSerializer(serializers.ModelSerializer):
    instance_id   = serializers.PrimaryKeyRelatedField(required=False,queryset=User.objects.all(),default=None)
    first_name       = serializers.CharField(required=True)
    last_name        = serializers.CharField(required=True)
    email            = serializers.EmailField(required=True)
    phone            = serializers.CharField(required=True)
    groups           = serializers.PrimaryKeyRelatedField(read_only=False, many=True, queryset=Group.objects.all(), required=False) 
    
    class Meta:
        model  = User
        fields = ['instance_id', 'first_name', 'last_name', 'email', 'phone', 'groups']
        
    def validate(self, attrs):
     
        phone    = attrs.get('phone')
        email    = attrs.get('email')
        instance_id    = attrs.get('instance_id')
        
        if not instance_id:
            if phone and email and User.objects.filter(phone=phone, email=email).exists():
                raise serializers.ValidationError({"error": ['Sorry, that phone number and email address is already in exists!']
                                                })
            
            if phone and User.objects.filter(phone=phone).exists():
                raise serializers.ValidationError({"error": ['Sorry, that phone number already exists!']})


            if email and User.objects.filter(email=email).exists():
                raise serializers.ValidationError({"error": ['Sorry, that email address already exists!']})
            
            return super().validate(attrs)
        else:
            if phone and email and User.objects.filter(phone=phone, email=email).exclude(id=instance_id.id).exists():
                raise serializers.ValidationError({"error": ['Sorry, that phone number and email address is already in exists!']
                                                })
            
            if phone and User.objects.filter(phone=phone).exclude(id=instance_id.id).exists():
                raise serializers.ValidationError({"error": ['Sorry, that phone number already exists!']})


            if email and User.objects.filter(email=email).exclude(id=instance_id.id).exists():
                raise serializers.ValidationError({"error": ['Sorry, that email address already exists!']})
            
            return super().validate(attrs)
    
    def create(self, validated_data):
        request = self.context.get('request')
        instance              = User()
        instance.first_name   = validated_data.get('first_name',None)
        instance.last_name    = validated_data.get('last_name',None)
        instance.phone        = validated_data.get('phone', None)
        instance.email        = validated_data.get('email',None)
        instance.is_admin     = True
        instance.save()
           

    def update(self, instance, validated_data):
        request               = self.context.get('request')
        instance.first_name   = validated_data.get('first_name',None)
        instance.last_name    = validated_data.get('last_name',None)
        instance.phone        = validated_data.get('phone',None)
        instance.email        = validated_data.get('email',None)
        instance.save()
        return instance
    

class ActiveOrInactivateAdminProfileSerializer(serializers.ModelSerializer):
    instance_id   = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),default=None)
    
    class Meta:
        model = User
        fields = ['instance_id']
        
    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance , validated_data):
        instance.is_active = True if not instance.is_active else False
        instance.save()
        return instance
    