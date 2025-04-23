import json
import os

from src.utils import read_json


def test_read_json():
    # 1. Подготовка тестовых данных
    test_data = {"test": 123}
    test_file = "temp_test.json"

    # 2. Создаем тестовый json-файл
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    # 3. Вызываем тестируемую функцию
    result = read_json(test_file)

    # 4. Проверяем результат
    assert result == test_data, "Функция вернула неверные данные"
    assert isinstance(result, dict), "Функция должна возвращать словарь"

    # 5. Убираем за собой
    os.remove(test_file)
    print("Тест пройден успешно!")
