from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from.models import Book

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the home page")

@permission_required('bookshelf.view_book, raise_exception=True')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

