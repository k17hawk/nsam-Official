from django.urls import path ,re_path
from .import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name='movetoblog'
urlpatterns = [
    path('blogs',views.BlogsView,name="blogs"),
    path('blogsdetail/<int:tk>/blogs/detail',views.BlogsdetailView,name="blogsdetail"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)