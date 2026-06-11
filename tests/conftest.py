import pytest

from src.category import Category
from src.product import Product
from src.product_classes import Smartphone, LawnGrass


@pytest.fixture
def product_1():
    return Product('apple', 'fruit', 14.5, 5)


@pytest.fixture
def product_2():
    return Product('tomato', 'vegetable', 20, 1)


@pytest.fixture
def category_1():
    return Category(
        name='food',
        description='fruit',
        products=[
            Product('apple', 'fruit', 1, 2),
            Product('banana', 'fruit', 3, 4)]
    )


@pytest.fixture
def category_2():
    return Category(
        name='food',
        description='vegetable',
        products=[
            Product('cucumber', 'fruit', 5, 6),
            Product('tomato', 'vegetable', 7, 8)]
    )


@pytest.fixture
def product_class_smartphone1():
    return Smartphone("Iphone 15", "512GB, Gray space", 10, 2, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_class_smartphone2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 10, 3, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def product_class_grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 10, 4, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_class_grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 10, 5, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_without_products():
    return Category(
        name='food1',
        description='fruit1'
    )