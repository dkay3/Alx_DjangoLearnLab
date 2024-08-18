from django.views.generic import ListView, DetailView
from .models import Book, Library  # Import Library here

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/list_libraries.html'
    context_object_name = 'libraries'


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
