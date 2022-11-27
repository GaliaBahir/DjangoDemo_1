from unittest import TestCase

from store.models import Product


class TestProductsModel(TestCase):
    def setUp(self):
        self.data1 = Product.objects.create(title='SW Alorithms', price='20.00')
        self.data2 = Product.objects.create(title='web applications tutorial', price='30.00')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(data.title, 'SW Alorithms')