from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("profiles.urls", namespace="profiles")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include(("quiz.urls", "quiz"), namespace="quiz")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
