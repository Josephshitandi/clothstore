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





