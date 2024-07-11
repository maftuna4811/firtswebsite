from django.shortcuts import render


def home_view(request):
    return render(request, 'blog.html')


def login_view(request):
    return render(request, 'auth/login.html')