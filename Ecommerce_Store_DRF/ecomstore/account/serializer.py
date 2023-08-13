from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','email','password','first_name','last_name')

    def get_email(self,obj):
        if self.context['request'].user.is_authenticated:
            return obj.email
        return None

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','email','password','first_name','last_name')

    #to check for the user credentials in backend
    #     create_user defined in models.py
    #   email and password already accessed in  create_user for extra feild first and last name use .get
    def create(self, validated_data):
        user = User.objects.create_user(
            # id=validated_data['id'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name =validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)

        user = UserSerializer(self.user)

        data.update({'user': user.data})

        return data