#coding: utf-8
from example.models import Book
from mongotest import MongoTestCase

class ExampleTestCase(MongoTestCase):
    def test_Book_creation(self):
        self.assertFalse(Book.objects())
        Book(name='The Book', pages=500).save()
        self.assertTrue(Book.objects())

    def test_if_database_is_clean(self):
        self.assertFalse(Book.objects())  
