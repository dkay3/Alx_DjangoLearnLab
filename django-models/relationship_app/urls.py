from django.urls import path
from .views import book_list, LibraryDetailView  # Import `book_list` here

urlpatterns = [
    path('books/', book_list, name='book_list'),  # Function-based view URL
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
]
