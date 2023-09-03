from rest_framework import serializers
from blog.models import Posts, Author, Tags


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"
        readonly = ["modified_at", "created_at", "deleted_at"]
