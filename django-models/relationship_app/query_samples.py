from django.db.models import Prefetch
from .models import Author, Book, Publisher

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None

# 2. List all books in a library (Assuming 'Publisher' represents a library in this context)
def list_all_books_in_library(library_name):
    try:
        publisher = Publisher.objects.get(name=library_name)
        books = publisher.books.all()
        return books
    except Publisher.DoesNotExist:
        return None

# 3. Retrieve the librarian for a library (Assuming a 'Profile' model linked to 'Author' represents the librarian)
def get_librarian_for_library(library_name):
    try:
        publisher = Publisher.objects.get(name=library_name)
        books = publisher.books.all()
        # Assuming that the librarian (Author) is the author of the first book in the library
        librarian = None
        if books.exists():
            librarian = books.first().author
        return librarian
    except Publisher.DoesNotExist:
        return None


from relationship_app.query_samples import get_books_by_author, list_all_books_in_library, get_librarian_for_library

# Example usage
books_by_author = get_books_by_author('Author Name')
all_books_in_library = list_all_books_in_library('Library Name')
librarian = get_librarian_for_library('Library Name')

print(books_by_author)
print(all_books_in_library)
print(librarian)
