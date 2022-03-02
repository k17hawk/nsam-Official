from django.contrib import admin
from .models import *

# Register your models here.

class SomeAdmin(admin.ModelAdmin):
      list_display = ( 'name',  'phone', 'email','date')
      list_filter = ['date']
admin.site.register(Contact,SomeAdmin)

