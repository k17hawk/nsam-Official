from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name='movetoevent'
urlpatterns = [
    path('event',views.EventView,name='event'),
    path('newsdetail/<int:tk>/news/detail',views.newsdetailView,name="newsdetail"),
  
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)            