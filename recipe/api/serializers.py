from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length = 255)
    # content = serializers.CharField
    # created_at = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Post.objects.create

    class Meta:
        model = Post
        fields = ('title', 'content')