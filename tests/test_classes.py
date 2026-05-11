import pytest

from src.classes import Product, Category


@pytest.fixture()
def product_1():
    return Product('apple', 'fruit', 14.5, 5)


def test_init_product_1(product_1):
    assert product_1.name == 'apple'
    assert product_1.description == 'fruit'
    assert product_1.price == 14.5
    assert product_1.quantity == 5


@pytest.fixture()
def product_2():
    return Product('tomato', 'vegetable', 20, 1)


def test_init_product_2(product_2):
    assert product_2.name == 'tomato'
    assert product_2.description == 'vegetable'
    assert product_2.price == 20
    assert product_2.quantity == 1


@pytest.fixture()
def category_1():
    return Category('food', 'fruit', ['apple', 'banana'])


def test_init_category_1(category_1):
    assert category_1.name == 'food'
    assert category_1.description == 'fruit'
    assert category_1.products == ['apple', 'banana']
    # Тест для подсчета категорий
    assert Category.category_count == 1
    # Тест для подсчета продуктов
    assert Category.product_count == 2

