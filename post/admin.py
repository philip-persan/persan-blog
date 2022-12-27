from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'author', 'title', 'date_created'
    list_display_links = 'id', 'author', 'title', 'date_created'
    list_filter = 'author',
    list_per_page = 40
