# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library


def book_list_view(request):
    books = Book.objects.select_related('author').all()
    response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response_text, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # You can also use plain text via HttpResponse
    context_object_name = 'library'
