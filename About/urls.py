from django.urls import path ,re_path
from . import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name='movetoabout'
urlpatterns = [
    path('aboutus',views.aboutViews,name="about"),
    path('ourteam',views.TeamViews,name="ourteam"),
    path('ourAdvisor',views.AdvisorViews,name="ourAdvisor"),
    path('ourPartners',views.PartnerViews,name="ourPartners"),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
