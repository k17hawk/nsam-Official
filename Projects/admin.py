from django.contrib import admin
from .models import *
# Register your models here.
class CompletedAdmin(admin.ModelAdmin):
    list_display = ['Heading',  'Project_Leader','Location','Funding_Agency']
    list_filter = ['date_And_time']
    
admin.site.register(Completed, CompletedAdmin)  

class OngoingdAdmin(admin.ModelAdmin):
    list_display = ['Heading',  'Project_Leader','Location','Funding_Agency']
    list_filter = ['date_And_time']
    
admin.site.register(Ongoing, OngoingdAdmin)  