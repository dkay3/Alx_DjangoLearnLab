from django.urls import path
from .views import (
    book_list, library_list, book_detail, library_detail,
    BookListView, LibraryListView, BookDetailView, LibraryDetailView
)

urlpatterns = [
    path('books/', ListBookView.as_view(), name='list_book'),
    path('libraries/', LibraryListView.as_view(), name='library_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
