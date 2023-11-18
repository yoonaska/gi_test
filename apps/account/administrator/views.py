from django.shortcuts import render
from apps.account.models import User
from apps.account.administrator.schemas import GetUsersResponseSchemas
from apps.account.administrator.serializers import ActiveOrInactivateAdminProfileSerializer, RegistrationSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from gi_test.helpers.response import ResponseInfo
from drf_yasg.utils import swagger_auto_schema
from gi_test.helpers.custom_messages import _success
from drf_yasg import openapi
from rest_framework import filters

class CreateOrUpdateRegisterAPIView(generics.GenericAPIView):
    
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(CreateOrUpdateRegisterAPIView, self).__init__(**kwargs)
    
    serializer_class = RegistrationSerializer
    
    @swagger_auto_schema(tags=["Admin Profile"])
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)

            instance = serializer.validated_data.get('instance_id',None)
            serializer = self.serializer_class(instance, data=request.data, context={'request': request})

            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"]      = False
                self.response_format["errors"]      = serializer.errors
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
        

class ActiveOrInactivateAdminProfileApiView(generics.GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ActiveOrInactivateAdminProfileApiView, self).__init__(**kwargs)

    serializer_class = ActiveOrInactivateAdminProfileSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=["Admin Profile"])
    def put(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code'] = status.HTTP_400_BAD_REQUEST
                self.response_format["status"] = False
                self.response_format["errors"] = serializer.errors
                return Response(self.response_format, status=status.HTTP_400_BAD_REQUEST)

            instance_id = serializer.validated_data.get('instance_id')
            serializer = self.serializer_class(instance_id, data=request.data, context={'request': request})

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
        

class GetUsersApiView(generics.ListAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(GetUsersApiView, self).__init__(**kwargs)

    queryset         = User.objects.filter().order_by('-id')
    serializer_class = GetUsersResponseSchemas
    filter_backends  = [filters.SearchFilter]
    # permission_classes = [IsAuthenticated]
    search_fields    = ['slug', 'email', 'first_name', 'last_name', 'phone']

    id = openapi.Parameter('id', openapi.IN_QUERY,
                                type=openapi.TYPE_INTEGER, required=False, description="Enter id")

    @swagger_auto_schema(tags=["Admin Profile"], manual_parameters=[id])
    def get(self, request, *args, **kwargs):
        queryset   = self.filter_queryset(self.get_queryset())
        instance_id = request.GET.get('id', None)
        if instance_id:
            queryset = queryset.filter(pk=instance_id)
        serializer = self.serializer_class(queryset, many=True)
        self.response_format['status'] = True
        self.response_format['data']   = serializer.data
        self.response_format['status_code'] = status.HTTP_200_OK
        return Response(self.response_format, status=status.HTTP_200_OK)
