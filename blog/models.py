from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.name
    

class Posts(models.Model):
    title = models.CharField(max_length=255, blank=False)
    summary = models.CharField(max_length=255, blank=True)
    content = models.CharField(max_length=1024, blank=False)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateTimeField(blank=True)
    
    author = models.ForeignKey("blog.Author", null=True, verbose_name=("Post_Author"), on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    