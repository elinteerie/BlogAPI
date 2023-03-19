from rest_framework import serializers
from django.contrib.auth import get_user_model 

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        
        model = Post
        
        
        
class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)