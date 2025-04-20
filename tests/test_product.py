import sys
from io import StringIO

from src.product import Product


def test_product_init(product_init):
    assert product_init.name == "Арбуз"
    assert product_init.price == 50.00
    assert product_init.description == "Ягода"
    assert product_init.quantity == 3


def test_new_product():
    prod = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})

    assert prod
    assert prod.name == "Samsung Galaxy S23 Ultra"
    assert prod.description == "256GB, Серый цвет, 200MP камера"


def test_price(product_init):
    assert product_init.price == 50.00

    product_init.price = 100.00
    assert product_init.price == 100.00

    product_init.price = 0
    product_init.price = -20.00
    assert product_init.price == 100.00
