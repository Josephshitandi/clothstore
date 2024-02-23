from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = ('id','username','user','avatar', 'address', 'phone_number','region')

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','user_type','email','first_name','last_name','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSignupSerializer, self).create(validated_data)

class LogoutSerializer(serializers.Serializer):
    refresh_token=serializers.CharField()
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category','image','card']

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = ['id','name','description','category','image2']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','item_name','price','date_added','sub_category','quantity','color','previous_price','size','brand','image','image2']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


