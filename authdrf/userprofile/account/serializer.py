from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        feilds = ('email','password','first_name','last_name')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        feilds = ('email','password','first_name','last_name')

    #to check for the user credentials in backend
    #     create_user defined in models.py
    #   email and password already accessed in  create_user for extra feild first and last name use .get
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name =validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        return user