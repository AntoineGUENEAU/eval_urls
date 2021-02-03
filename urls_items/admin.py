from django.contrib import admin
from .models import Url

# Register your models here.
class UrlItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_filter = ['name', 'url']
    list_editable = ['name', 'url', ]
    search_fields = ['name', 'url',]

admin.site.register(Url, UrlItemAdmin)