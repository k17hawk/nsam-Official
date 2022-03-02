from django.urls import path ,re_path
from .import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


app_name='movetoproject'
urlpatterns = [
    path('project',views.ProjectsView,name="projects"),
    path('ongoing',views.OngoingView,name="ongoing"),
    path('completed',views.CompletedView,name="completed"),
    path('completed',views.CompletedView,name="completed"),
    path('detailcompleted/<int:pk>/project/completed',views.detailcompletedview,name="detailcompleted"),
    path('detailongoing/<int:sk>/project/ongoing',views.detailongoingview,name="detailongoing"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)