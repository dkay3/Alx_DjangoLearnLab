from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register  # Import `book_list` here

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]


