"""
URL configuration for news project.

"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from newsapp import views
from frontendapp import urls as frontend_urls
router = DefaultRouter()

router.register(r'berita', views.BeritaViewSet)
router.register(r'komentar', views.KomentarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include(frontend_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)