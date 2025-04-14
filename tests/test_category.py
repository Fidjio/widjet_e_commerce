def test_category_init(category_init_1, category_init_2):
    assert category_init_1.name == "Продовольствие"
    assert category_init_1.description == "Товары для питания"
    assert len(category_init_1.products) == 2

    assert category_init_1.count_category == 2
    assert category_init_2.count_category == 2

    assert category_init_1.count_products == 5
    assert category_init_2.count_products == 5
