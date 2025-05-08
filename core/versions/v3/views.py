from django.shortcuts import get_object_or_404
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from ...serializers import PostListSerializer
from ..v2.serializers import DetailSerializer
from ...models import Post

class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = DetailSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return DetailSerializer
        return PostListSerializer

    def get_queryset(self):
        published_posts = self.queryset.filter(publish = True)
        return published_posts
    
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return DetailSerializer
        return PostListSerializer