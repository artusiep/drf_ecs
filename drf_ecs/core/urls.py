from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.views import health_check

schema_view = get_schema_view(
    openapi.Info(
        title="drf_ecs Api Documentation",
        default_version='v1',
        description="API Documentation",
        contact=openapi.Contact(email="email@domain.com"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)
swagger_patterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('/auth/', include('rest_framework.urls')),
]

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('admin/', admin.site.urls),
    path('swagger', include(swagger_patterns)),
    path('status', health_check, name='health_check'),
]
