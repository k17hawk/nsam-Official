from django.contrib import admin
from .models import *
# Register your models here.


class publicdAdmin(admin.ModelAdmin):
    list_display = ['title',  'date_And_time']
    list_filter = ['date_And_time']
    
admin.site.register(PublicHealth, publicdAdmin)  

class EduAdmin(admin.ModelAdmin):
    list_display = ['title',  'date_And_time']
    list_filter = ['date_And_time']
    
admin.site.register(EducationAwarness, EduAdmin)   

class ResAdmin(admin.ModelAdmin):
    list_display = ['title',  'date_And_time']
    list_filter = ['date_And_time']
    
admin.site.register(Workshop, ResAdmin)  

class disAdmin(admin.ModelAdmin):
    list_display = ['title',  'date_And_time']
    list_filter = ['date_And_time']
    
admin.site.register(wildlife, disAdmin)  



