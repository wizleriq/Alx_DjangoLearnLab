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
