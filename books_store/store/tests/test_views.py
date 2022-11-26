import json
import django.http as Http
from unittest import TestCase
from django.test import Client
from store.models import Product
from store.views import all_products


class StoreViewsTestCase(TestCase):
    def test_calculate_discount(self):
        client = Client()
        response = client.patch("/store/",
            json.dumps({"price": 60,"discount": 20}),
        )
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertEqual(response_json["calculated_price"], 48.0)
            
            
    def test_homepage_html(self):
        request = Http.HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
