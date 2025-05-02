from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ...models import Post
from accounts.models import CustomUser


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', "content","author", "created_on"] 

class DetailSerializer(ModelSerializer):
    title = serializers.CharField(required = False)
    content = serializers.CharField(required = False)

    class Meta:
        model = Post
        fields = ['title', "content","author", "publish", "created_on"]