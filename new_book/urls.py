from django.urls import path
from .views import home, login, register, books, author

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('books/', books, name='books'),
    path('author/', author, name='author')
]