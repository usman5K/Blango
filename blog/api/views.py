from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blog.api.serializers import PostSerializer, PostDetailSerializer
from blog.models import Posts
from rest_framework.permissions import IsAdminUser


class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostDetailSerializer
    permissions_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]