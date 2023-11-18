from rest_framework import serializers
from apps.home.models import Note
from gi_test.helpers.helpers import ConvertBase64File, get_token_user_or_none






class CreateOrUpdateNoteSerializers(serializers.ModelSerializer):

    instance_id   = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(),required=False,help_text="This api need only when updating")
    title         = serializers.CharField(required=True)
    description   = serializers.CharField(required=False)
    
    class Meta:
        model =  Note
        fields = ['instance_id','title','description']   

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
               
        request                 = self.context.get('request')
        instance                = Note()
        instance.title          = validated_data.get('title',None)
        instance.description    = validated_data.get('description',None)
        instance.created_by     = get_token_user_or_none(request)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request                 = self.context.get('request')
        instance.title          = validated_data.get('title',None)
        instance.description    = validated_data.get('description',None)
        instance.created_by     = get_token_user_or_none(request)
        instance.save()
        return instance



class DestroyNoteSerializer(serializers.ModelSerializer):
    
    instance_id = serializers.PrimaryKeyRelatedField(queryset=Note.objects.all(),many=True,required=True)
    
    class Meta:
        model = Note
        fields = ['instance_id']







