from django.contrib import admin
from .models import Cinema
from .models import Viewers


class CinemaList(admin.ModelAdmin):
    list_display = ('name', 'director', 'release_date')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ['name']


class ViewersList(admin.ModelAdmin):
    list_display = ('viewer_name', 'email')
    list_filter = ('viewer_name',)
    search_fields = ('viewer_name',)
    ordering = ['viewer_name']


# Register your models here.
admin.site.register(Cinema)
admin.site.register(Viewers)
