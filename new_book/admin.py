from django.contrib import admin
from .models import Book, Author, Comments

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comments)

