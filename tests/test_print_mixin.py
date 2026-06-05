from src.product import Product
from src.product_classes import Smartphone, LawnGrass

def test_print_mixin(capsys):
    Product('apple', 'fruit', 1, 2)
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Product(apple, fruit, 1, 2)'

    Smartphone("Iphone 15", "512GB, Gray space", 10, 2, 98.2, "15", 512, "Gray space")
    massage = capsys.readouterr()
    assert massage.out.strip() == 'Smartphone(Iphone 15, 512GB, Gray space, 10, 2)'

    LawnGrass("Газонная трава", "Элитная трава для газона", 10, 4, "Россия", "7 дней", "Зеленый")
    massage = capsys.readouterr()
    assert massage.out.strip() == 'LawnGrass(Газонная трава, Элитная трава для газона, 10, 4)'

