"""Contains unit tests for the views"""
import unittest
from expensify import app

class ViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page_loads(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)