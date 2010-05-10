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
    db_name = 'test_%s' % settings.NOSQL_DATABASE_NAME
    def _pre_setup(self):
        super(MongoEngineTestCase, self)._pre_setup()
        connect(self.db_name)

    def _post_teardown(self):
        super(MongoEngineTestCase, self)._post_teardown()
        con = Connection()
        con.drop_database(self.db_name)

