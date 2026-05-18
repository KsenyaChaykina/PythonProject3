import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_1():
    return Product('apple', 'fruit', 14.5, 5)


@pytest.fixture()
def product_2():
    return Product('tomato', 'vegetable', 20, 1)


@pytest.fixture()
def category_1():
    return Category(
        name='food',
        description='fruit',
        products=[
            Product('apple', 'fruit', 1,2),
            Product('banana', 'fruit',3,4)]
    )

@pytest.fixture()
def category_2():
    return Category(
        name='food',
        description='vegetable',
        products=[
            Product('cucumber', 'fruit',5,6),
            Product('tomato', 'vegetable',7,8)]
    )