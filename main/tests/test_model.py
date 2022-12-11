from django.test import TestCase
from decimal import Decimal
from main import models


class TestModel(TestCase):
    def test_active_manager_works(self):
        models.Product.objects.create(
            name="The Cathedral and the bazaar",
            price=Decimal("10.00")
        )
        models.Product.objects.create(
            name="Pride and Prejudice",
            price=Decimal("2.00")
        )
        models.Product.objects.create(
            name="A Tale of Two Cities",
            price=Decimal("2.00"),
            active=False
        )
        self.assertEqual(len(models.Product.objects.active()), 2)
