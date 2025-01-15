from django.contrib import admin
from django.urls import path, include
from app.custom.drf_yasg import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
    path("api/v1/", include("authentication.urls")),
]
