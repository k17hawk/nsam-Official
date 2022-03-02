from django.contrib import admin
from .models import *
admin.site.register(SlideImage)
# Register your models here.
class SubAdmin(admin.ModelAdmin):
	list_display = ( 'name',  'date', 'email')
	list_filter = ['date']
admin.site.register(Subscriber,SubAdmin)