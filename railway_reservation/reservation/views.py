from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import login,authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
# Create your views here.
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            if created:
                token.delete()
                token=Token.objects.create(user=user)
            return Response({'token':token.key,'username':user.username,'role':user.role})
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        print(request.headers)
        token_key=request.auth.key
        token=Token.objects.get(key=token_key)
        return Response({'detail':'User successfully logged out.'})