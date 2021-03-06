from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email']
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        print(validated_data)
        return super().create(validated_data)


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_profile = UserProfile.objects.get(pk=data['user_profile'])
        serialized = UserProfileSerializer(instance=user_profile)
        data['user_profile'] = serialized.data
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    # If for some reason this is throwing an error, change 'id' to 'user'  
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = User.objects.get(pk=data['id'])
        serialized = UserSerializer(instance=user)
        data['id'] = serialized.data
        return data

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = User.objects.get(pk=data['user'])
        serialized = UserSerializer(instance=user)
        data['user'] = serialized.data
        return data

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = User.objects.get(pk=data['user'])
        serialized = UserSerializer(instance=user)
        data['user'] = serialized.data
        return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = User.objects.get(pk=data['user'])
        serialized = UserSerializer(instance=user)
        data['user'] = serialized.data
        return data

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = User.objects.get(pk=data['user'])
        serialized = UserSerializer(instance=user)
        data['user'] = serialized.data
        return data