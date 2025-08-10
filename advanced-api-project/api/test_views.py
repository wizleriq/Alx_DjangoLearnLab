from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create some books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author_id=1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2018, author_id=1)

        # URLs
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.details_url = reverse('book-detail', args=[self.book1.id])
        self.update_url = reverse('book-update', args=[self.book1.id])
        self.delete_url = reverse('book-delete', args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_detail_book(self):
        response = self.client.get(self.details_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book One")

    def test_create_book_requires_auth(self):
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "publication_year": 2023,
            "author": 1
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
            # "author": 1
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.put(self.update_url, {
            "title": "Updated Book",
            "publication_year": 2021,
            "author": 1
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_with_auth(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books(self):
        response = self.client.get(f"{self.list_url}?title=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Book Two")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(
            response.data[0]['publication_year'],
            response.data[1]['publication_year']
        )







# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from django.contrib.auth.models import User
# from .models import Book

# class BookAPITestCase(APITestCase):
#     def setup(self):
#         # Create a user
#         self.user = User.Objects.create_user(username="testuser", password="password123")
#         self.client = APIClient()

#         # Create some books
#         self.book1 = Book.objects.creat(title="Book One", publication_year=2020, author_id=1)
#         self.book2 = Book.objects.create(title="Book Two", publication_year=2018, author_id=1)

#         # URLS
#         self.list_url = reverse('book-list')
#         self.create_url = reverse('book-create')
#         self.details_url = reverse('book-detail', args=[self.book1.id])
#         self.update_url = reverse('book-update', args=[self.book1.id])
#         self.delete_url = reverse('book-delete', args=[self.book1.id])

#         def test_list_books(self):
#             response = self.client.get(self.list_url)
#             self.assertEual(response.status_code, status.HTTP_200_OK)
#             self. assertGreaterEqual(len(response.data), 2)

#         def test_detail_book(self):
#             response = self.client.get(self.detail.url)
#             self.assertEqual(response.status_code, status.HTTP_200_OK)
#             self.assertEqual(response.data['title'], "Book One")

#         def test_create_book_requires_auth(self):
#             response = self.client.post(self.create_url, {
#             "title": "New Book",
#             "publication_year": 2023,
#             "author": 1
#         })
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

#     def test_create_book_with_auth(self):
#         self.client.login(username="testuser", password="password123")
#         response = self.client.post(self.create_url, {
#             "title": "New Book",
#             "publication_year": 2023,
#             "author": 1
#         })
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Book.objects.count(), 3)

#     def test_update_book_with_auth(self):
#         self.client.login(username="testuser", password="password123")
#         response = self.client.put(self.update_url, {
#             "title": "Updated Book",
#             "publication_year": 2021,
#             "author": 1
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.book1.refresh_from_db()
#         self.assertEqual(self.book1.title, "Updated Book")

#     def test_delete_book_with_auth(self):
#         self.client.login(username="testuser", password="password123")
#         response = self.client.delete(self.delete_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

#     def test_filter_books(self):
#         response = self.client.get(f"{self.list_url}?title=Book One")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_search_books(self):
#         response = self.client.get(f"{self.list_url}?search=Book Two")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_order_books(self):
#         response = self.client.get(f"{self.list_url}?ordering=-publication_year")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertGreaterEqual(response.data[0]['publication_year'], response.data[1]['publication_year'])
        
