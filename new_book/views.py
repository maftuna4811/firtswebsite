from django.shortcuts import render

from new_book.models import Book, Author


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(tittle__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, "value": search, 'message': "Successfully"})
        else:
            return render(request, 'books.html', {'message': "Not fount"})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book, "message": "Successfully"})
    else:
        return render(request, 'book_detail.html', {"message": "Not Fount"})


def author(request):
    author = Author.objects.all()
    context = {'all_authors': author}
    return render(request, 'author.html', context=context)



