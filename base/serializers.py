from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class UserSerializer(serializers.ModelSerializer):
    # favourited_by = serializers.StringRelatedField()
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # favourited_by = serializers.StringRelatedField()
    class Meta:
        model = Post
        # fields = ['id', 'username', 'email', 'first_name', 'last_name']
        fields = '__all__'