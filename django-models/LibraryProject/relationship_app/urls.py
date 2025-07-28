# from django.urls import path
# from .views import book_list_view, LibraryDetailView

# urlpatterns = [
#     path('books/', book_list_view, name='book-list'),
#     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
# ]


# from django.urls import path
# from .views import list_books, LibraryDetailView  

# urlpatterns = [
#     path('books/', list_books, name='list_books'),  
#     path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 
# ]

from django.urls import path
from .views import register_view, login_view, logout_view, LibraryDetailView, book_list_view

urlpatterns = [
    path('books/', book_list_view, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Auth views
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

