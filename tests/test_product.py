def test_product_init(product_init):
    assert product_init.name == "Арбуз"
    assert product_init.price == 50.00
    assert product_init.description == "Ягода"
    assert product_init.quantity == 3
