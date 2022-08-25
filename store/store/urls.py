from os import name

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:    # если работаем локально
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
