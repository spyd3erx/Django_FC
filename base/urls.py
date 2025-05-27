from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
]

if settings.DEBUG:
   urlpatterns += debug_toolbar_urls() #primero se condigura el debug toolbar
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #luego los medias
