from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from gi_test.helpers.response import ResponseInfo
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics,status
from rest_framework.response import Response
from apps.account.models import User
from django.contrib import auth
from gi_test.helpers.custom_messages import _account_tem_suspended,_invalid_credentials
import json
from gi_test import settings
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from gi_test.helpers.helpers import DataEncryption
from django.db.models import Q


# App Login Start

# End Logout
