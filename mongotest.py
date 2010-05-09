#coding: utf-8
from pymongo import Connection
from django.test.simple import *
from django.test import TestCase
from django.conf import settings

from mongoengine import connect
from mongoengine.connection import _get_db

__all__ = ['MongoEngineTestRunner', 'MongoEngineTestCase']

class MongoEngineTestRunner(DjangoTestSuiteRunner):

    db_name = settings.NOSQL_DATABASE_NAME

    def setup_databases(self, **kwargs):
        connect(self.db_name)
        print 'Creating mongodb test database: ' + self.db_name

        return super(MongoEngineTestRunner, self).setup_databases()

    def teardown_databases(self, old_config):

        super(MongoEngineTestRunner, self).teardown_databases(old_config)
        conn = Connection()
        conn.drop_database(self.db_name)
        print 'Destroying mongodb test database: ' + self.db_name

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

