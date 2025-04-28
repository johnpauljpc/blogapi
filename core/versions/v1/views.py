from django.shortcuts import render, get_object_or_404
from rest_framework import status, response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ...models import Post
from ...serializers import PostListSerializer

# Create your views here.
@api_view()
def post_list(request):
    qs = Post.objects.all()
    serializer = PostListSerializer(qs, many = True)
    return response.Response(serializer.data)

@api_view(http_method_names=["POST"])
def create_post(request):
    serializer = PostListSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(http_method_names=["GET"])
def post_detail(request, pk):
    queryset = get_object_or_404(Post, id = pk)
    serializer = PostListSerializer(queryset)
    return Response(serializer.data)

@api_view(http_method_names=["post", "update"])
def post_update(request, pk):
    post = get_object_or_404(Post, id = pk)
    serializer = PostListSerializer(post, data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(http_method_names=['get', 'delete'])
def post_delete(request, pk):
    post = get_object_or_404(Post, id = pk)
    post_title = post.title
    serializer = PostListSerializer(post)
    if request.method == "DELETE":
        post.delete()
        return Response({"msg": f"{post_title} deleted sucessfully!"})
    return Response(serializer.data)