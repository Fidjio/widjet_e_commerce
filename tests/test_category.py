from src.product import Product


def test_category_init(category_init_1, category_init_2):
    assert category_init_1.name == "Продовольствие"
    assert category_init_1.description == "Товары для питания"
    assert len(category_init_1.products_list) == 2

    assert category_init_1.count_category == 2
    assert category_init_2.count_category == 2

    assert category_init_1.count_products == 5
    assert category_init_2.count_products == 5


def test_add_product(category_init_1):
    prod1 = Product("Перчик", "Овощ", 2000.00, 99)
    category_init_1.add_product(prod1)
    assert category_init_1.products == (
                                        'Арбуз, 50.0 руб. Остаток: 3 шт.\n'
                                        'Картошка, 25.0 руб. Остаток: 2 шт.\n'
                                        'Перчик, 2000.0 руб. Остаток: 99 шт.\n'
    )


def test_products(category_init_1):
    assert category_init_1.products == ('Арбуз, 50.0 руб. Остаток: 3 шт.\n'
                                        'Картошка, 25.0 руб. Остаток: 2 шт.\n')


def test_products_list(category_init_1):
    assert category_init_1.products_list
    assert len(category_init_1.products_list) == 2
