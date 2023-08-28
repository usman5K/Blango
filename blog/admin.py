from django.contrib import admin
from blog.models import Posts, Author


# Register your models here.
admin.site.register([Posts, Author])