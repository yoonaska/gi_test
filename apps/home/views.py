import logging
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import filters
from apps.home.schemas import  NoteApiListingApiSchemas
from apps.home.serializers import   CreateOrUpdateNoteSerializers, DestroyNoteSerializer
from gi_test.helpers.pagination import RestPagination
from gi_test.helpers.response import ResponseInfo
from gi_test.helpers.custom_messages import _success
from apps.home.models import Note
logger = logging.getLogger(__name__)




"""--------- Note MANAGEMENT SECTION APIS----------------"""


class NotesListApiView(generics.ListAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(NotesListApiView, self).__init__(**kwargs)

    queryset            = Note.objects.filter().order_by('-id')
    serializer_class    = NoteApiListingApiSchemas
    pagination_class    = RestPagination
    filter_backends     = [filters.SearchFilter]
    search_fields       = ['slug','tile']

    id = openapi.Parameter('id', openapi.IN_QUERY,
                                type=openapi.TYPE_INTEGER, required=False, description="Enter id")
    
    @swagger_auto_schema(pagination_class=RestPagination,tags=["Notes (Admin)"],manual_parameters=[id])
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        instance_id       = request.GET.get('id', None)
        
        if instance_id :
            queryset = queryset.filter(pk=instance_id)
        
        serializer = self.serializer_class(queryset, many=True,context={'request': request})
        self.response_format['status'] = True
        self.response_format['data'] = serializer.data
        self.response_format['status_code'] = status.HTTP_200_OK
        return Response(self.response_format, status=status.HTTP_200_OK)



class CreateOrUpdateNotesApiView(generics.GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateNotesApiView, self).__init__(**kwargs)

    serializer_class = CreateOrUpdateNoteSerializers

    @swagger_auto_schema(tags=["Notes (Admin)"])
    def post(self, request):
        try:
            serializer = self .serializer_class(data=request.data,context={'request':request})
            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)
            
            instance = serializer.validated_data.get('instance_id',None)
            serializer = self.serializer_class(instance, data=request.data, context={'request': request})
            
            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            self.response_format['status_code'] = status.HTTP_201_CREATED
            self.response_format["message"] = _success
            self.response_format["status"] = True
            return Response(self.response_format, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            self.response_format['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status'] = False
            self.response_format['message'] = str(e)
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class DestroyNotesApiView(generics.GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(DestroyNotesApiView, self).__init__(**kwargs)

    serializer_class = DestroyNoteSerializer

    @swagger_auto_schema(tags=["Notes (Admin)"], request_body=serializer_class)
    def delete(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():

                instance_ids = serializer.validated_data['instance_id']

                for instance in instance_ids:
                    instance.delete()

                self.response_format['status_code'] = status.HTTP_200_OK
                self.response_format["message"] = _success
                self.response_format["status"] = True
                return Response(self.response_format, status=status.HTTP_200_OK)

            else:
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            self.response_format['status_code'] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format['status'] = False
            self.response_format['message'] = str(e)
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



