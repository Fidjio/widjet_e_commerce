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
