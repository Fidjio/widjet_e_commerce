import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category_init_1():
    prod1 = Product("Арбуз", "Ягода", 50.00, 3)
    prod2 = Product("Картошка", "Овощ", 25.00, 2)
    result_category = Category("Продовольствие", "Товары для питания", [prod1, prod2])

    return result_category


@pytest.fixture
def category_init_2():
    prod1 = Product("Клубника", "Ягода", 50.00, 3)
    prod2 = Product("Вишня", "Ягода", 25.00, 2)
    prod3 = Product("Огурец", "Овощ", 85.00, 5)
    result_category = Category("Продовольствие", "Товары для питания", [prod1, prod2, prod3])

    return result_category


@pytest.fixture
def product_init():
    prod1 = Product("Арбуз", "Ягода", 50.00, 3)

    return prod1
