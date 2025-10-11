from django.test import TestCase
from restaurant.models import Menu, Booking, MenuItem

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Test Menu",
            description="Test Description",
            price=9.99,
            inventory=100
        )

    def test_menu_item_creation(self):
        self.assertEqual(self.menu_item.title, "Test Menu")
        self.assertEqual(self.menu_item.description, "Test Description")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertEqual(self.menu_item.inventory, 100)
