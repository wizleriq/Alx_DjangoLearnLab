Create Book Instance
command

from bookshelf.models import Book book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) book

output:

<Book: 1984>