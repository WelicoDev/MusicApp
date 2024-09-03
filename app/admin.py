from django.contrib import admin
from .models import Music, Artist

# Register your models here.


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'duration')
    list_display_links = ('id', 'title' , 'duration')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age')
    list_display_links = ('id', 'first_name', 'last_name')