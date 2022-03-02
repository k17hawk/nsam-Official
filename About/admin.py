from django.contrib import admin
from .models import *

admin.site.register(OurTeam)
admin.site.register(Advisor)


class MultipleDonarAdmin(admin.StackedInline):
    model = Image_multiple_Donar

@admin.register(Donars_and_partners)
class ImageAdmin(admin.ModelAdmin):
    inlines = [MultipleDonarAdmin]

    class Meta:
       model = Donars_and_partners


class MultipleDonarAdmin(admin.ModelAdmin):
     pass
  