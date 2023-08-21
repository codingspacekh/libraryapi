from django.test import TestCase
from django.urls import reverse

from .models import Book
# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="a good title",
            subtitle="a good subtitle",
            author="an author",
            isbn="9876543210999",
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "a good title")
        self.assertEqual(self.book.subtitle, "a good subtitle")
        self.assertEqual(self.book.author, "an author")
        self.assertEqual(self.book.isbn, "9876543210999")
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "good subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")