from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.generics import CreateAPIView, GenericAPIView, DestroyAPIView

# Create your views here.
class RegisterUserView(APIView):
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    serializer_class = UserSerializer
    def post(self, request):

        # if email is already in use
        if CustomUser.objects.filter(email=request.data['email']).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            user_info = {
                "id":new_user.id,
                "email": new_user.email
            }
            return Response(user_info, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileViewAndUpdate(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class=UserSerializer
    queryset = UserProfile.objects.all()
    
    def get(self, request):
        user = CustomUser.objects.get(email=request.user.email)
        print(user)
        user =  self.serializer_class(user).data
        return Response(user, status=status.HTTP_200_OK)
    def patch(self, request):
        profile = UserProfile.objects.get(user=request.user)
        
        serializer = UserProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)