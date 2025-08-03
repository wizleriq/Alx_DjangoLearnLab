from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from.models import Book
from .forms import ExampleForm

# Create your views here.
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_void():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return HttpResponse(f"Thanks, {name}!")
    else:
        form = ExampleForm()

    return render(request, 'example_template.html', {'form': form})

def home(request):
    return HttpResponse("Welcome to the home page")

@permission_required('bookshelf.view_book, raise_exception=True')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

