from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *
 
 
class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Resource_Video, PostAdmin)


class MultipleImageAdmin(admin.StackedInline):
    model = Image_multiple

@admin.register(Image_Resource)
class ImageAdmin(admin.ModelAdmin):
    inlines = [MultipleImageAdmin]

    class Meta:
       model = Image_Resource


class MultipleImageAdmin(admin.ModelAdmin):
     pass



class MultiplePosterAdmin(admin.StackedInline):
    model = Poster_multiple

@admin.register(Poster_Resource)
class ImageAdmin(admin.ModelAdmin):
    inlines = [MultiplePosterAdmin]

    class Meta:
       model = Poster_Resource


class MultiplePosterAdmin(admin.ModelAdmin):
     pass
admin.site.register(Report)     