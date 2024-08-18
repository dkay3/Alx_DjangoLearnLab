from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout
from django.contrib.auth.views import LoginView, LogoutView  # Import `book_list` here
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view URL
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view URL
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')), 
]


