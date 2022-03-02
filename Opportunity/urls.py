from django.urls import path ,re_path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name='movetooppo'
urlpatterns = [
    path('Opportunity',views.OppoViews,name="Opportunity"),
    path('Membership',views.InternViews,name="Membership"),
    path('Volunteer',views.VolunterViews,name="Volunteer"),

  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
