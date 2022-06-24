from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import status
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','email','mobile')
        extra_kwargs = {
            'password':{'write_only': True},'email':{'required':True},
        }

    def create(self, validated_data):
        user = User.object.create_user(username = validated_data['username'],password = validated_data['password'],email=validated_data['email'],mobile =validated_data['mobile'])
        return user