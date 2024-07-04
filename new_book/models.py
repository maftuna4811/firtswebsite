from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    tittle = models.CharField(max_length=200)
    info = models.TextField()
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    books = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text





