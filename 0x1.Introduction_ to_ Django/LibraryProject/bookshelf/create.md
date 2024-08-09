# Import the Book model
from bookshelf.models import Book

# Create a new Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)

# Save the instance to the database
book.save()

# Verify that the instance was created
print(book)

# 1984 by George Orwell, and publication year 1949.
