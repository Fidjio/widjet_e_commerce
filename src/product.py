class Product:
    """ Класс для описания продукта """
    name: str
    description: str
    price: float
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == '__main__':
    prod1 = Product('Арбуз', 'Сочный и красный', 100.00, 2)

    print(prod1.name, prod1.price, prod1.quantity, prod1.description)
