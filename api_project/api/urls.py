from django.urls import path, include
from .views import BookViewSet
# from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    # path('api/book/', BookList.as_view(), name='book-list'),
    path('api/', include(router.urls)),
]
# urlpatterns = [
#     path('api/book/', BookList.as_view(), name='book-list'),
#     path('api/book/create/', BookCreate.as_view(), name='book-create'),
#     path('api/book/<int:pk>/', BookDetail.as_view(), name='book-detail'),
# ]




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
