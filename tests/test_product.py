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
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

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


def test_magic_str_product():
    product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, "14")

    assert str(product1) == f"Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert product1 + product2 == 2114000.0
    assert product1 + product3 == "Price или quantity не является числом!"
