from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
User = get_user_model()#shortcut - whatever the current usermodel is, use that

class UserSerializer(serializers.ModelSerializer): #validates incoming user from request and puts them in the database

    password = serializers.CharField(write_only=True) 
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})

        try:
            validations.validate_password(password=password)
        except ValidationError as err:
            raise serializers.ValidationError({'password': err.messages})

        data['password'] = make_password(password) #setting user pw = where we store the user password
        return data#returns new user with password object on it

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'password_confirmation',)#would not tuypcially want to display the password in serializer format