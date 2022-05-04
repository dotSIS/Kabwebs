from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from api.models import Blog

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer