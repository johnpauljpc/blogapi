from rest_framework.serializers import ModelSerializer
from ...models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', "content","author", "created_on"] 

class DetailSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', "content","author", "publish", "created_on"]