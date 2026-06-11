import pytest

from src.category import Category
from src.product import Product


def test_init_category_1(category_1, category_2):
    assert category_1.name == 'food'
    assert category_1.description == 'fruit'
    assert category_2.name == 'food'
    assert category_2.description == 'vegetable'
    # Тест для подсчета категорий
    assert Category.category_count == 2
    # Тест для подсчета продуктов
    assert Category.product_count == 4


def test_products_property(product_1, product_2):
    category = Category('food', 'vegetable', [product_1, product_2])
    assert category.products == 'apple, 14.5 руб. Остаток: 5 шт.\ntomato, 20 руб. Остаток: 1 шт.\n'


def test_category_str(category_1, category_2):
    assert str(category_1) == 'food, количество продуктов: 6'
    assert str(category_2) == 'food, количество продуктов: 14'


def test_middle_price(category_1, category_without_products):
    assert category_1.middle_price() == 2
    assert category_without_products.middle_price() == 0


def test_add_product(category_1):
    new_product = Product('apple', 'fruit', 2, 4)
    category_1.add_product(new_product)

    assert new_product in category_1._Category__products
    assert Category.product_count >= 3


def test_add_product_type_error(category_1):
    with pytest.raises(TypeError):
        category_1.add_product("Неверный тип данных")
