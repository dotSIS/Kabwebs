from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Blog

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'blogs']
        
class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'author']