from django.urls import path
from . import views

from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

app_name='home'
urlpatterns = [
    path("", views.home, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)