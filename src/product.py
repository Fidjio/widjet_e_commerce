from typing import Any, Dict


class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> str | float | Any:
        try:
            full_sum_prod = (self.__price * self.quantity) + (other.__price * other.quantity)
            return full_sum_prod
        except TypeError:
            return 'Price или quantity не является числом!'

    @classmethod
    def new_product(cls, setting_dict: Dict[str, Any]) -> "Product":
        """Создает новый продукт из словаря"""
        return cls(**setting_dict)

    @property
    def price(self) -> float:
        """Геттер для цены продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для установки новой цены продукта с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

