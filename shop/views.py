from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import viewsets,status,generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from django.http import HttpResponse, Http404
import json
from rest_framework import filters  
from rest_framework.generics import ListAPIView
from rest_framework import mixins

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,IsCustomerOrAdmin]
    serializer_class = UserSignupSerializer