from django.shortcuts import render, get_object_or_404
from .models import Book, Library

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/list_libraries.html', {'libraries': libraries})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})
