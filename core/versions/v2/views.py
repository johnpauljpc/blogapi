from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...models import Post
from .serializers import PostListSerializer
from .serializers import DetailSerializer

class ListCreatePost(APIView):
    def get(self, request):
        queryset = Post.objects.filter(publish = True)
        serializer = PostListSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DetailSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostDetail(APIView):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        serializer = DetailSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        serializer = DetailSerializer(post, data = request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
    
    def delete(self, request, slug):
        post = get_object_or_404(Post, slug = slug)
        title = post.title
        post.delete()
        return Response({"msg": f"{title} deleted!"})