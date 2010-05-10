#coding: utf-8
from pymongo import Connection
from django.test.simple import *
from django.test import TestCase
from django.conf import settings

from mongoengine import connect
from mongoengine.connection import _get_db

__all__ = ['MongoEngineTestRunner', 'MongoEngineTestCase']

class MongoEngineTestCase(TestCase):
    """
    TestCase class that clear the collection between the tests
    """
    def _clear_mongodb(self):
        con = Connection()
        db_name = settings.NOSQL_DATABASE_NAME
        con.drop_database(db_name)
        connect(db_name)

    def _pre_setup(self):
        super(MongoEngineTestCase, self)._pre_setup()
        self._clear_mongodb()

    def _post_teardown(self):
        super(MongoEngineTestCase, self)._post_teardown()
        self._clear_mongodb()

