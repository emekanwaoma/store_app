from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Item


class APITestCase(APITestCase):
    def test_get_items(self):
        url = reverse("item-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_suppliers(self):
        url = reverse("supplier-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        url = reverse("item-list")
        data = {"name": "New Item", "description": "New Description", "price": "12.99", "suppliers": []}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_create_supplier(self):
        url = reverse("supplier-list")
        data = {"name": "New Supplier", "contact": "New Contact Info"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_create_item_with_invalid_supplier(self):
        url = reverse("item-list")
        data = {
            "name": "Test Item",
            "description": "This is a test item",
            "price": 100,
            "suppliers": [1],  # One invalid supplier ID
        }
        response = self.client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Item.objects.count(), 0)
        self.assertIn("suppliers", response.data)
