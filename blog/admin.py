from django.contrib import admin
from blog.models import Posts, Author, Comment, Tags


# Register your models here.
admin.site.register([Posts, Author, Comment, Tags])