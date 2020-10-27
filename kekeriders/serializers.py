from kekeriders.models import Kekerider 
from rest_framework import serializers, status
# from models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='password',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # def __str__(self):
    #     return self.user


class KekeriderSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    class Meta:
        model = Kekerider
        fields = ('user', 'phone_number', 'address',
                  'location', 'license')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(
            UserSerializer(), validated_data=user_data)
        kekerider, created = Kekerider.objects.update_or_create(user=user,
                                                                 phone_number=validated_data.pop(
                                                                     'phone_number'),
                                                                 address=validated_data.pop(
                                                                     'address'),
                                                                 location=validated_data.pop(
                                                                     'location'),
                                                                 license=validated_data.pop(
                                                                     'license'),
                                                                 )
        return kekerider



