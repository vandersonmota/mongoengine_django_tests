#coding: utf-8
from pymongo import Connection
from django.test.simple import *
from django.test import TestCase
from django.conf import settings

from mongoengine import connect
from mongoengine.connection import _get_db

__all__ = ['MongoEngineTestCase']

class MongoEngineTestCase(TestCase):
    """
    TestCase class that clear the collection between the tests
    """
    db_name = 'test_%s' % settings.NOSQL_DATABASE_NAME
    def __init__(self, methodName='runtest'):
        self.db = connect(self.db_name)
        super(MongoEngineTestCase, self).__init__(methodName)

    def _post_teardown(self):
        super(MongoEngineTestCase, self)._post_teardown()
        for collection in self.db.collection_names():
            if collection == 'system.indexes':
                continue
            self.db.drop_collection(collection)
