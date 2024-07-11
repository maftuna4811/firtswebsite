from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    info = models.TextField()
    birth_date = models.DateTimeField(auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    tittle = models.CharField(max_length=200)
    image = models.ImageField()
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    page = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
