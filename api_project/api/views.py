from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """
     BookViewSet provides CRUD operations for Book model.
    Authentication:
        - Requires token authentication
        - Only authenticated users can access endpoints
    Permissions:
        - IsAuthenticated: non-authenticated requests will be denied

        """

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookCreate(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDetail(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer



# # class BookListAPIView(generics.ListAPIView):
# #     queryset = BookModel.objects.all()
# #     serializer_class = BookSerializer

# # class BookCreateAPIView(generics.CreateAPIView):
# #     queryset = BookModel.objects.all()
# #     serializer_class = BookSerializer


