from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("swiftspaces/auth/", include("apps.accounts.urls")),
    # path("swiftspaces/properties/", include("apps.properties.urls")),
    # path("swiftspaces/profiles/", include("apps.profiles.urls")),
    # django-debug-toolbar
    path("__debug__/", include(debug_toolbar.urls)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
