# tests/test_django_index.py
from django.test import TestCase, Client


class IndexViewTest(TestCase):
    def test_index_returns_200(self):
        """Test that the index view returns a 200 status code"""
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)