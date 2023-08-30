from rest_framework import serializers
from blog.models import Posts


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields = "__all__"
    readonly = ["modified_at", "created_at"]

