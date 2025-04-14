from src.product import Product


class Category:
    name: str
    description: str
    products: list

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []


if __name__ == '__main__':
    prod1 = Product('Арбуз', 'Сочный и красный', 100.00, 2)
    warehouse1 = Category('Ягоды', 'Все ягоды магазина', prod1)

    print(warehouse1.name, warehouse1.description, warehouse1.products)
