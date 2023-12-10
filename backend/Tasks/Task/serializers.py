from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meeta:
        model= User
        fields=['username','password']
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ListModel
        fields='__all__'

