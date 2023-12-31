from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Tags(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    value = models.TextField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=255, blank=False)
    summary = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=1024, blank=False)
    slug = models.SlugField(unique=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, null=True, blank=True, related_name="post_tags")
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey("blog.Author", null=True, verbose_name=("Post_Author"), on_delete=models.SET_NULL)
    comments = models.ForeignKey("blog.Comment", null=True, verbose_name=("Post_Comments"), on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=512)
    creator = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="Creator_Comments")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.body