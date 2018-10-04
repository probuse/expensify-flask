"""Contains unit tests for the views"""
import unittest
from expensify import app

class ViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page_loads(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_returns_right_content(self):
        response = self.app.get('/login', content_type='html/text')
        self.assertIn(b'Please Login', response.data)