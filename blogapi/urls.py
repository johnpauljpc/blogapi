
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/blog/", include("core.versions.v1.urls") ),
    path("api/v2/blog/", include("core.versions.v2.urls") ),
    path("api/v3/blog/", include("core.versions.v3.urls") ),
]
