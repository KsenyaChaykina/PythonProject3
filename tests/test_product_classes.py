import pytest

def test_product_class_smartphone_init(product_class_smartphone1):
    assert product_class_smartphone1.name == "Iphone 15"
    assert product_class_smartphone1.description == "512GB, Gray space"
    assert product_class_smartphone1.price == 10
    assert product_class_smartphone1.quantity == 2
    assert product_class_smartphone1.color == "Gray space"
    assert product_class_smartphone1.efficiency == 98.2
    assert product_class_smartphone1.model == "15"
    assert product_class_smartphone1.memory == 512

def test_product_class_grass_init(product_class_grass2):
    assert product_class_grass2.name == "Газонная трава 2"
    assert product_class_grass2.description == "Выносливая трава"
    assert product_class_grass2.price == 10
    assert product_class_grass2.quantity == 5
    assert product_class_grass2.color == "Темно-зеленый"
    assert product_class_grass2.country == "США"
    assert product_class_grass2.germination_period == "5 дней"

def test_class_smartphone_add(product_class_smartphone1, product_class_smartphone2):
    assert product_class_smartphone1 + product_class_smartphone2 == 50

def test_class_grass_add(product_class_grass1, product_class_grass2):
    assert product_class_grass1 + product_class_grass2 == 90

def test_class_add_error(product_class_smartphone1, product_class_grass1):
    with pytest.raises(TypeError):
        result = product_class_smartphone1 + 1
    with pytest.raises(TypeError):
        result2 = product_class_smartphone1 + product_class_grass1