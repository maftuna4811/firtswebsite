from django.contrib import admin
from .models import Author, Book, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date", "created_at")
    list_display_links = ('first_name', 'last_name')
    search_fields = ("first_name", "last_name")
    ordering = ("id", "first_name", "last_name", "birth_date", "created_at")


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'tittle', 'info', 'count', 'price', 'created_at')
    list_display_links = ('tittle',)
    search_fields = ('id', "tittle", )
    ordering = ("id", "tittle")
    prepopulated_fields = {'slug': ('tittle',)}


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', "user", "text", "created_at")
    list_display_links = ('user',)
    search_fields = ('id', 'user', )
    ordering = ("id", 'text')












