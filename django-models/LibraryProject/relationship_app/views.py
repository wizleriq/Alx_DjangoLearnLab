# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib import messages
# from .models import Book  # If you have a Book model
# from django.contrib.auth.decorators import login_required


# # List all books – example view that requires login
# @login_required
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})


# # Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('list_books')  # redirect to your desired page
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'relationship_app/login.html', {'form': form})


# # Logout View
# def logout_view(request):
#     logout(request)
#     return render(request, 'relationship_app/logout.html')


# # Registration View
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('list_books')  # redirect to your desired page
#         else:
#             messages.error(request, 'Registration failed. Please correct the errors below.')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})







#  # from django.shortcuts import render
# # # from django.views.generic.detail import DetailView
# # # from .models import Book, Library

# # # # Function-based view to list all books
# # # def list_books(request):
# # #     books = Book.objects.all()  # Task expects this exactly
# # #     return render(request, "relationship_app/list_books.html", {"books": books})

# # # # Class-based view for Library detail
# # # class LibraryDetailView(DetailView):
# # #     model = Library
# # #     template_name = 'relationship_app/library_detail.html'
# # #     context_object_name = 'library'

# # from django.shortcuts import render, redirect
# # from django.contrib.auth import authenticate, login, logout
# # from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# # from django.contrib.auth.decorators import login_required

# # # Register
# # def register_view(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('login')
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'relationship_app/register.html', {'form': form})

# # # Login
# # def login_view(request):
# #     if request.method == 'POST':
# #         form = AuthenticationForm(data=request.POST)
# #         if form.is_valid():
# #             user = form.get_user()
# #             login(request, user)
# #             return redirect('library_detail', pk=1)  # Or redirect to any authenticated page
# #     else:
# #         form = AuthenticationForm()
# #     return render(request, 'relationship_app/login.html', {'form': form})

# # # Logout
# # def logout_view(request):
# #     logout(request)
# #     return render(request, 'relationship_app/logout.html')







# # # # from django.shortcuts import render

# # # # # Create your views here.
# # # from django.shortcuts import render
# # # from django.http import HttpResponse
# # # from .models import Book
# # # from django.views.generic.detail import DetailView
# # # from .models import Library


# # # def book_list_view(request):
# # #     books = Book.objects.select_related('author').all()
# # #     response_text = "\n".join([f"{book.title} by {book.author.name}" for book in books])
# # #     return HttpResponse(response_text, content_type="text/plain")


# # # class LibraryDetailView(DetailView):
# # #     model = Library
# # #     template_name = 'relationship_app/library_detail.html'  # You can also use plain text via HttpResponse
# # #     context_object_name = 'library'



# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from .models import Book  # or remove if you haven’t created this yet

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('list_books')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# def list_books(request):
#     return render(request, 'relationship_app/list_books.html')


from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# Register view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # or your home page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

