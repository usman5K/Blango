from rest_framework import serializers
from blog.models import Posts, Author, Tags, Comment


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("name", "id")


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Posts
        fields = "__all__"
        readonly = ["modified_at", "created_at", "deleted_at",
         "author", "tags", "comments", "published_at", "slug"]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "body", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer()

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments")

        instance = super(PostDetailSerializer, self).update(instance, validated_data)

        for comment_data in comments:
            if comment_data.get("id"):
                # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.post = instance
            comment.save()

        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"
        