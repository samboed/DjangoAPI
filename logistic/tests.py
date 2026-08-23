from django.test import TestCase
from rest_framework.test import APIClient


class Tests(TestCase):
    def test_sample_view(self):
        url = '/api/v1/test'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
