from django.contrib import admin
from .models import Highlights,Gallery

class HighlightsAdmin(admin.ModelAdmin):
    list_display = ['img']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['img']

admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Highlights,HighlightsAdmin)