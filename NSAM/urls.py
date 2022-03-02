from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from error import views as myviews
from django.conf.urls import handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace= "movetohome")),
    path('blog/', include('Blogs.urls',namespace= "movetoblog")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('event/', include('events.urls',namespace= "movetoevent")),
    path('contact/', include('Contact.urls',namespace= "movetocontact")),
    path('opportunity/', include('Opportunity.urls',namespace= "movetooppp")),
    path('programme/', include('Programmes.urls',namespace= "movetoprogram")),
    path('project/', include('Projects.urls',namespace= "movetoproject")),
    path('resource/', include('Resources.urls',namespace= "movetoresource")),
    path('about/', include('About.urls',namespace= "movetoabout")),
]
handler404 = myviews.error_404
handler500 = myviews.error_500  
if settings.DEBUG:    
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  