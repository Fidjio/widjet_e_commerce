import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict[Any, Any] | Any:
    """Открывает json-файл и возвращает словарь"""
    path_to_file = os.path.abspath(path)
    with open(path_to_file, "r", encoding="UTF-8") as f:
        data = json.load(f)

    return data


def create_object_for_json(data: dict) -> list:
    """Создает объекты по классам Product и Category с помощью словаря"""
    categories = []

    for cat in data:
        products = []
        for prod in cat["products"]:
            products.append(Product(**prod))

        cat["products"] = products
        categories.append(Category(**cat))

    return categories
