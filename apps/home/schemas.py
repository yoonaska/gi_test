from rest_framework import serializers
from apps.home.models import Note


"""----  LISTING API"""
class NoteApiListingApiSchemas(serializers.ModelSerializer):
    
    class Meta:
        model = Note 
        fields = ['id','title','description','is_active',]
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in data.keys():
            try:
                if data[field] is None:
                    data[field] = ""
            except KeyError:
                pass
        return data