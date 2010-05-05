from django.db import models
from mongoengine import Document, StringField, IntField

class Book(Document):
    author = StringField(max_length=30)
    pages = IntField()
