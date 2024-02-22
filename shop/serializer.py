from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = ('id','username','user','avatar', 'address', 'phone_number','region')

        