from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import ListView, DetailView
from .models import Book, Library

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_book.html', {'books': books})

def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'relationship_app/library_detail.html', {'library': library})


class ListBookView(ListView):
    model = Book
    template_name = 'relationship_app/list_book.html'
    context_object_name = 'books'

class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'

class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/book_detail.html'
    context_object_name = 'book'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    