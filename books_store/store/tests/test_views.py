import json
import django.http as Http
from unittest import TestCase
from django.test import Client


class StoreViewsTestCase(TestCase):
    def test_post(self):
        try:
            client = Client()
            response = client.patch('/store/')
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.content)
        except:
            self.assertEqual(response.status_code, Http.HttpResponseServerError.status_code)
