# # from django.urls import path
# # from .views import book_list_view, LibraryDetailView

# # urlpatterns = [
# #     path('books/', book_list_view, name='book-list'),
# #     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
# # ]


# # from django.urls import path
# # from .views import list_books, LibraryDetailView  

# # urlpatterns = [
# #     path('books/', list_books, name='list_books'),  
# #     path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
# # ]

# from django.urls import path
# from .views import register_view, login_view, logout_view, LibraryDetailView, book_list_view

# urlpatterns = [
#     path('books/', book_list_view, name='list_books'),
#     path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

#     # Auth views
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
