from django.urls import path
from .views import home, login, register, books, author, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('books/', books, name='books'),
    path('books/<slug:slug>/', book_detail, name='book-detail'),
    path('author/', author, name='author')
]