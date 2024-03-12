from django.urls import path, include
from MyUserAuth import urls as myuserauth_urls
from workouts import urls as workouts_urls
from django.contrib import admin

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Description of your API",
        # Add contact and license information if desired
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Allow public access for Swagger docs
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Include Django Admin URLs
    path("myuserauth/", include(myuserauth_urls)),  # Include MyUserAuth app's urlpatterns
    path("workouts/", include(workouts_urls)),  # Include workouts app's urlpatterns
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Add Swagger UI view
]