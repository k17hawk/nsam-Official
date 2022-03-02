from django.urls import path ,re_path
from .import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

app_name='movetoresource'
urlpatterns = [
    path('resources',views.ResourcesView,name="resources"),
    path('Videos&photos',views.PhotosView,name="Videos&photos"),
    path('brouchers',views.brouchersView,name="brouchers"),
    path('report',views.ReportView,name="report"),
    path('results',csrf_exempt(views.SearchView),name='searchbar'),  

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)