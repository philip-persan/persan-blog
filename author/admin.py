from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'user', 'profissao', 'nivel', 'sexo', 'pais', 'estado'
    list_display_links = 'user', 'profissao', 'nivel'
    list_filter = ['profissao', 'nivel', 'pais', 'estado']
    list_per_page = 40
