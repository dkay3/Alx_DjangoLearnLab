from django.shortcuts import render

# Create your views here.

# bookshelf/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Handle book editing logic
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle book creation logic
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})


# bookshelf/views.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    permission_required = 'bookshelf.can_create'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    permission_required = 'bookshelf.can_edit'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'bookshelf.can_delete'
    success_url = '/books/'


# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExampleForm
from .models import Book

def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list')
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})




# views.py
from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("Hello, World!")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://ajax.googleapis.com; style-src 'self' https://fonts.googleapis.com"
    return response
