from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from blog.api.views import PostViewSet, TagViewSet
from rest_framework.authtoken import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(router.urls)),
]
