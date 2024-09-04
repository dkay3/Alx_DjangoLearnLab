from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

class BookTests(APITestCase):
    def setUp(self):
        """Set up initial data for tests"""
        self.client = Client()
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Book Title",
            publication_year=2024,
            author=self.author
        )
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_book_authenticated(self):
        """Test creating a new book with an authenticated user"""
        data = {
            'title': 'New Book Title',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book Title')

    def test_create_book_unauthenticated(self):
        """Test creating a new book with an unauthenticated user"""
        self.client.logout()  # Ensure the user is logged out
        data = {
            'title': 'New Book Title',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_read_book(self):
        """Test retrieving a book"""
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating a book"""
        data = {'title': 'Updated Title'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url + '?title=Book%20Title', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        """Test searching for books"""
        response = self.client.get(self.list_url + '?search=Book', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        """Test ordering books"""
        response = self.client.get(self.list_url + '?ordering=title', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data['results']]
        self.assertEqual(titles, sorted(titles))
