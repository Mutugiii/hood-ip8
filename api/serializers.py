from rest_framework import serializers
from .models import User, Post, Profile, Hood, EmergencyService, Bussiness
from django.contrib.auth.hashers import make_password



def required(value):
    '''Function to have a field as required'''
    if value is None:
        raise serializers.ValidationError('This field is required')

class UserSerializer(serializers.ModelSerializer):
    '''Serializer for user Model'''
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password')
    
    def validate_password(self, value: str) -> str:
        return make_password(value)

class HoodSerializer(serializers.ModelSerializer):
    '''Serializer for Hood Model'''
    admin = serializers.StringRelatedField(read_only=True)
    location = serializers.CharField(validators=[required])
    class Meta:
        model = Hood
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    '''Serializer for profile Model'''
    user = serializers.StringRelatedField(read_only=True)
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    '''Serializer for Post Model'''
    user = serializers.StringRelatedField(read_only=True)
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class BussinessSerializer(serializers.ModelSerializer):
    '''Serializer for Bussiness class'''
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Bussiness
        fields = '__all__'


class EmergencyServiceSerializer(serializers.ModelSerializer):
    '''Serializer for Bussiness class'''
    hood = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = EmergencyService
        fields = '__all__'