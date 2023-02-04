from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.contrib.auth.models import User
# Create your views here.


class PostModelViewSet(viewsets.ModelViewSet):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()