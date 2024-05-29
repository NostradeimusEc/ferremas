from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import HomeView, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    path('accounts/', include('allauth.urls')),

    path('users/', include('accounts.urls', namespace='users')),

    path('', HomeView.as_view(), name="home"),
    path('products/<slug>/', ProductDetailView.as_view(), name="product-detail"),

    path('marketplace/', include ('marketplace.urls', namespace="marketplace")),

    path("__reload__/", include("django_browser_reload.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)