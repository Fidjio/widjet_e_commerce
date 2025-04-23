from typing import List, Optional

from src.product import Product


class Category:
    name: str
    description: str
    count_category = 0
    count_products = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.count_category += 1
        Category.count_products += len(products) if products else 0

    def __str__(self):
        all_quantity = 0
        all_quantity += sum([product.quantity for product in self.__products])

        return f'Название категории, количество продуктов: {all_quantity} шт.'

    def add_product(self, new_product: Product) -> None:
        self.__products.append(new_product)
        Category.count_products += 1

    @property
    def products(self) -> str:
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return products_str

    @property
    def products_list(self) -> List[Product]:
        return self.__products
