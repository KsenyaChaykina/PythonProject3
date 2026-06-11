import pytest

from src.product import Product


def test_init_product_1(product_1):
    """ Тест успешного создания товара """
    assert product_1.name == 'apple'
    assert product_1.description == 'fruit'
    assert product_1.price == 14.5
    assert product_1.quantity == 5


def test_init_product_2(product_2):
    """ Тест успешного создания товара """
    assert product_2.name == 'tomato'
    assert product_2.description == 'vegetable'
    assert product_2.price == 20
    assert product_2.quantity == 1


def test_product_creation_negative_quantity():
    """ Отрицательное количество должно вызывать ошибку """
    with pytest.raises(ValueError) as exc_info:
        Product("apple", "fruit", 120, -1)
    assert str(exc_info.value) == 'Товар с нулевым количеством не может быть добавлен'


def test_product_price(capsys, product_1):
    product_1.price = -30
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-1] == 'Цена не должна быть нулевая или отрицательная'
    product_1.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip().split("\n")[-1] == 'Цена не должна быть нулевая или отрицательная'
    product_1.price = 40
    assert product_1.price == 40


def test_new_product():
    """ Проверка успешного создания объекта при корректных данных """
    new_product = Product.new_product({"name": "carrot", "description": "vegetable", "price": 40, "quantity": 5})
    assert isinstance(new_product, Product)
    assert new_product.name == "carrot"
    assert new_product.price == 40
    assert new_product.description == "vegetable"
    assert new_product.quantity == 5


def test_new_product_missing_argument():
    """ Проверка ошибки: в словаре не хватает обязательного поля 'price' """
    new_product = Product.new_product({"name": "carrot"})
    assert isinstance(new_product, set)
    assert len(new_product) == 1
    error = list(new_product)[0]
    assert isinstance(error, TypeError)


def test_new_product_unexpected_argument():
    """Проверка ошибки: передан лишний аргумент, которого нет в __init__"""
    new_product = Product.new_product({"name": "Чехол", "price": 1000, "color": "черный"})
    assert isinstance(new_product, set)
    error = list(new_product)[0]
    assert isinstance(error, TypeError)


def test_product_str(product_1, product_2, category_1):
    assert str(product_1) == 'apple, 14.5 руб. Остаток: 5 шт.'
    assert str(product_2) == 'tomato, 20 руб. Остаток: 1 шт.'


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 92.5
