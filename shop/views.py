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
    # permission_classes = [IsAuthenticated,IsCustomerOrAdmin]
    serializer_class = UserSignupSerializer

class SignupAPIView(generics.GenericAPIView):
    serializer_class = UserSignupSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSignupSerializer(user,context=self.get_serializer_context()).data,
            # "token": AuthToken.objects.create(user)[1]
        })
    
class LogoutAPIView(generics.CreateAPIView):
    serializer_class=LogoutSerializer
    permission_classes=(IsAuthenticated,)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token=request.data.get('refresh_token')
        error_message={
            "error":"Token is invalid or expired"
        }
        success_message={
            "success":"Logout successfully"
        }        
        try:
            token=RefreshToken(token)
            token.blacklist()
        except TokenError as error:
            return Response(error_message,status=status.HTTP_400_BAD_REQUEST)
        return Response(success_message,status=status.HTTP_200_OK)
    
class ProductViewSet(APIView):
    def get(self, request, format=None):      
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        permission_classes = [IsAuthenticated,IsAdmin]
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ProductDetail(APIView):
    """
    Retrieve, update or delete product instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        permission_classes = [IsAuthenticated, IsAdmin]
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        permission_classes = [IsAuthenticated, IsAdmin]
        product = self.get_object(pk)
        ProductSerializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
