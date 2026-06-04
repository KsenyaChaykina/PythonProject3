from src.category import Category


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
