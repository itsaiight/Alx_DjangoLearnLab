from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        self.book1 = Book.objects.create(
            title="Harry Potter",
            author="J.K. Rowling",
            published_date="2000-07-08"
        )
        self.book2 = Book.objects.create(
            title="The Hobbit",
            author="J.R.R. Tolkien",
            published_date="1937-09-21"
        )

    def test_list_books(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "1984",
            "author": "George Orwell",
            "published_date": "1949-06-08"
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "1984")

    def test_retrieve_book(self):
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "author": "J.K. Rowling",
            "published_date": "2000-07-08"
        }
        response = self.client.put(reverse('book-update', kwargs={'pk': self.book1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'])

    def test_delete_book(self):
        response = self.client.delete(reverse('book-delete', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get("/books/?title__icontains=harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get("/books/?search=Hobbit")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_date(self):
        response = self.client.get("/books/?ordering=published_date")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First one should be the oldest (The Hobbit)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    def test_unauthenticated_create_fails(self):
        self.client.logout()
        data = {
            "title": "Brave New World",
            "author": "Aldous Huxley",
            "published_date": "1932-01-01"
        }
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
