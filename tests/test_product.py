from src.product import Product


def test_init_product_1(product_1):
    assert product_1.name == 'apple'
    assert product_1.description == 'fruit'
    assert product_1.price == 14.5
    assert product_1.quantity == 5


def test_init_product_2(product_2):
    assert product_2.name == 'tomato'
    assert product_2.description == 'vegetable'
    assert product_2.price == 20
    assert product_2.quantity == 1

def test_product_price(capsys, product_1):
    product_1.price = -30
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    product_1.price = 0
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Цена не должна быть нулевая или отрицательная'
    product_1.price = 40
    assert product_1.price == 40

def test_new_product():
    new_product = Product.new_product({"name": "carrot", "description": "vegetable", "price": 40, "quantity": 5})
    assert new_product.name == "carrot"
    assert new_product.price == 40
    assert new_product.description == "vegetable"
    assert new_product.quantity == 5
