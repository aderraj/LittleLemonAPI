from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(
            title="Test Pizza",
            description="Delicious test pizza",
            price=12.99,
            inventory=25
        )
        self.menu_item2 = Menu.objects.create(
            title="Test Pasta",
            description="Amazing test pasta",
            price=15.50,
            inventory=30
        )
        self.menu_item3 = Menu.objects.create(
            title="Test Salad",
            description="Fresh test salad",
            price=8.75,
            inventory=20
        )

    def test_getall(self):

        response = self.client.get('/restaurant/menu/')

        menu_items = Menu.objects.all()

        serialized_data = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serialized_data.data)

