# Book API – View Configurations

## Overview
This API provides CRUD operations for managing books.
It is built using Django REST Framework and follows RESTful design principles.

## Permissions
- ListView (GET /api/books/) → Public
- DetailView (GET /api/books/<id>/) → Public
- CreateView (POST /api/books/create/) → Authenticated users only
- UpdateView (PUT /api/books/update/<id>/) → Authenticated users only
- DeleteView (DELETE /api/books/delete/<id>/) → Authenticated users only

## Custom Behavior
- CreateView validates that the book title is unique before saving.
- UpdateView prevents saving books with a `publication_year` earlier than 1500.
- All authenticated-only endpoints use `IsAuthenticated` permission class.

## Testing
Use Postman or curl to test:
1. GET (List & Detail) without authentication
2. POST, PUT, DELETE with and without authentication to verify permission rules.


Filtering, Searching, and Ordering in Book API
Filtering: Use exact matches on fields like title, author, and publication_year.
Example: /api/books/?author=Jane Austen&publication_year=1813

Searching: Use the search query param to perform partial text matches on title and author.
Example: /api/books/?search=pride

Ordering: Use the ordering query param to sort results by title or publication_year.

Ascending order: /api/books/?ordering=title

Descending order: /api/books/?ordering=-publication_year

