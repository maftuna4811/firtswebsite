from django.contrib import admin
from django.contrib.admin import ModelAdmin

from blog.models import Author, Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'info', 'birth_date', 'created_at')
    list_display_links = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'text', 'author', 'page', 'created_at')
    list_display_links = ('tittle',)
    ordering = ('tittle',)





