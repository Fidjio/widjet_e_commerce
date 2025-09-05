from typing import Any, Dict
from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: "Product") -> str | float | Any:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, setting_dict: Dict[str, Any]) -> "Product":
        """Создает новый продукт из словаря"""
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        """Геттер для цены продукта"""
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Сеттер для установки новой цены продукта с проверкой"""
        pass


class Product(BaseProduct):
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
            if type(other) is self.__class__:
                full_sum_prod = (self.__price * self.quantity) + (other.__price * other.quantity)
                return full_sum_prod
        except TypeError:
            return 'Price или quantity не является числом!'

        raise TypeError('Сложение разных видов товара невозможно!')



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

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: str, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

