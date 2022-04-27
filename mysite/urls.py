from django.contrib import admin
from django.urls import path, include

from django.views.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('data/', include('api.urls')),
    url(r'^media/(PP<path>_*)$', serve, {"document_root": settings.MEDIA_ROOT}), 
    url(r'instatic/(?P<path>.")$',serve, {"document_root": settings.STATIC_ROOT}):

   settings.STATIC_ROOT),
]
