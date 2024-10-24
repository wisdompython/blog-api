from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser  
        fields=("email", "password", "confirm_password")
        extra_kwargs = {'password': {'write_only': True}, 
                        "confirm_password":{'write_only':True}}
        
    def validate(self, attrs):
        if not attrs['email'].endswith("@bytewave-technlogies.com"):
            raise serializers.ValidationError(
            {"invalid mail": "You need a company email to register"})
            
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        try:
            validate_password(attrs['password'])
        except ValidationError as err:
            raise serializers.ValidationError(
            {"password": err.messages})
        return attrs
    
    def create(self, validated_data):
        
        new_user = CustomUser.objects.create(
            email = validated_data['email'],
        )
        new_profile = UserProfile.objects.create(user=new_user)
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user
# Serializer for updating user profile
class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(required=False)
    profile_pic = serializers.ImageField(required=False)
    class Meta:
        model = UserProfile
        fields = ['name','profile_pic','email']
    
    def validate(self, attrs):
        if not attrs['email'].endswith("@bytewave-technlogies.com"):
            raise serializers.ValidationError(
            {"invalid mail": "You need a company email to register"})
        return attrs
    
    def update(self, instance, validated_data):
        print(instance.user.email)
        instance.user.email = validated_data.get('email', instance.user.email)
        instance.user.save()
        print(instance.user.email)
        instance.name = validated_data.get("name", instance.name)
        instance.profile_pic = validated_data.get("profile_pic", instance.profile_pic)
        instance.save()
        
        return instance
        
        