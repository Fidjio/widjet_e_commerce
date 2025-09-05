import sys
from io import StringIO

import pytest

from src.product import Product, LawnGrass, Smartphone
#
#
# def test_product_init(product_init):
#     assert product_init.name == "Арбуз"
#     assert product_init.price == 50.00
#     assert product_init.description == "Ягода"
#     assert product_init.quantity == 3
#
#
# def test_new_product():
#     prod = Product.new_product(
#         {
#             "name": "Samsung Galaxy S23 Ultra",
#             "description": "256GB, Серый цвет, 200MP камера",
#             "price": 180000.0,
#             "quantity": 5,
#         }
#     )
#
#     assert prod
#     assert prod.name == "Samsung Galaxy S23 Ultra"
#     assert prod.description == "256GB, Серый цвет, 200MP камера"
#
#
# def test_price(product_init):
#     assert product_init.price == 50.00
#
#     product_init.price = 100.00
#     assert product_init.price == 100.00
#
#     product_init.price = 0
#     product_init.price = -20.00
#     assert product_init.price == 100.00
#
#
# def test_magic_str_product():
#     product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, "14")
#
#     assert str(product1) == f"Iphone 15, 210000.0 руб. Остаток: 8 шт."
#     assert product1 + product2 == 2114000.0
#     assert product1 + product3 == "Price или quantity не является числом!"
#
#
# def test_add_product():
#     product1 = Product("Iphone 15", "512GB, Gray space", 100.0, 2)
#     product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 200.0, 1)
#     lawn_grass = LawnGrass("test", "тестовый класс", 150.0, 1, "Russia", "10 дней", "White")
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
#                              "S23 Ultra", 256, "Серый")
#
#     assert product1 + product2 == 400.0
#     with pytest.raises(TypeError, match="Сложение разных видов товара невозможно!"):
#         lawn_grass + product1
#         lawn_grass + smartphone1
#
#
# def test_init_lawngrass():
#     grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#
#     assert grass1.color == "Зеленый"
#     assert grass1.country == "Россия"
#     assert grass1.germination_period == "7 дней"
#
# def test_init_smartphone():
#     smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
#                              "S23 Ultra", 256, "Серый")
#
#     assert  smartphone1.efficiency == 95.5
#     assert  smartphone1.memory == 256
#     assert  smartphone1.model == "S23 Ultra"
#     assert  smartphone1.color == "Серый"

def test_init_print_mixin(capsys):
    prod1 = Product("Арбуз", "Ягода", 50.00, 3)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Арбуз, 50.0, Ягода, 3)'

    lawn_grass = LawnGrass("test", "тестовый класс", 150.0, 1, "Russia", "10 дней", "White")
    message = capsys.readouterr()
    assert message.out.strip() == 'LawnGrass(test, 150.0, тестовый класс, 1)'

    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    message = capsys.readouterr()
    assert message.out.strip() == 'Smartphone(Samsung Galaxy S23 Ultra, 180000.0, 256GB, Серый цвет, 200MP камера, 5)'
