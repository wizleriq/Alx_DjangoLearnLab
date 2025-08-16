from django.urls import path
from .views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('api/book/', BookList.as_view(), name='book-list'),
    path('api/book/create/', BookCreate.as_view(), name='book-create'),
    path('api/book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]




# from django.urls import path
# from .views import BookCreate,BookList

# urlpatterns = [
#     path('api/book/', BookList.as_view(), name='book-list'),
#     path('api/book/create/', BookCreate.as_view(), name='book-create')

# ]

# from django.urls import path
# from .views import BookCreateAPIView, BookListAPIView

# urlpatterns = [
#     path('api/books/', BookListAPIView.as_view(), name='book-list'),
#     path('api/books/create/', BookCreateAPIView.as_view(), name='book-create'),
# ]
